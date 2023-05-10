'''
All 13 metrics you collect will be on a “per node” basis.
You will be calculating three categories of metrics:
	- Data size metrics (8 metrics)
		These metrics indicates how manypackets a node sends/receive and the
		related amount of data/bytes sent/received
			1. Number of Echo Requests sent
			2. Number of Echo Requests received
			3. Number of Echo Replies sent
			4. Number of Echo Replies received
			5. Total Echo Request bytes sent
				In bytes, based on the size of the “frame”
			6. Total Echo Request bytes received
				In bytes, based on the size of the “frame”
			7. Total Echo Request data sent
				In bytes, based on amount of data in the ICMP payload
			8. Total Echo Request data received
				In bytes, based on amount of data in the ICMP payload

	- Time based metrics (4 metrics)
			1. Average Ping Round Trip Time (RTT)
				– Ping RTT is defined as the time between sending an 
				Echo Request packet and receiving a corresponding Echo 
				Reply packet from the destination
				– Measured in milliseconds

			2. Echo Request Throughput (in kB/sec)
				- Defined as the sum of the frame sizes of all 
				Echo Request packets sent by the node divided by 
				the sum of all Ping RTTs

			3. Echo Request Goodput (in kB/sec)
				- Defined as the sum of the ICMP payloads of
				all Echo Request packets sent by the node
				divided by the sum of all Ping RTTs

			4. Average Reply Delay (in microseconds)
				- Defined as the time between a node
				receiving an Echo Request packet and
				sending an Echo Reply packet back to the
				source
'''

files = ['../Captures/Node1_parsed.txt', '../Captures/Node2_parsed.txt', '../Captures/Node3_parsed.txt', '../Captures/Node4_parsed.txt']


def compute_RTT(request_time_list, reply_time_list, request_bytes_sent, numb_of_requests_sent, num_of_replys_sent, request_data_size, request_time_2, reply_time_2):
		total_round_trip = 0
		delay = 0
		total_hop_count = 0

	
		for request_packet_time in request_time_list:
			for reply_packet_time in reply_time_list:

				reply_num = int(reply_packet_time[0])
				request_num = int(request_packet_time[0])

				request_ttl = int(request_packet_time[2])
				reply_ttl = int(reply_packet_time[2])

				
				if(reply_num == request_num):
					total_round_trip += (float(reply_packet_time[1]) - float(request_packet_time[1])) 
					
					
					if(request_ttl == reply_ttl):
						total_hop_count += 1
					else:
						total_hop_count += 3
		
		for reply_packet in reply_time_2:
			for request_packet in request_time_2:
				reply_number = int(reply_packet[0])
				request_number = int(request_packet[0])


				if(request_number == reply_number):
					delay += float(float(reply_packet[1]) - float(request_packet[1]))


		throughput = round((request_bytes_sent / total_round_trip) * 0.001, 1)
		goodput = round((request_data_size / total_round_trip) * 0.001, 1)
		average_hop_count = round(total_hop_count / numb_of_requests_sent,2)
		RTT = round((total_round_trip / numb_of_requests_sent) * 1000, 2)
		reply_delay = round(delay / num_of_replys_sent  * 1000000 , 2)

		print(f"\nAverage RTT (milliseconds),{RTT}")
		print(f"Echo Request Throughput (kB/sec),{throughput}")
		print(f"Echo Request Goodput (kB/sec),{goodput}")
		print(f"Average Reply Delay (microseconds),{reply_delay}")
		print(f"Average Echo Request Hop Count,{average_hop_count}" + "\n")
		#print(delay)
	
def compute():
	# Data Size Metrics
	#ECHO Requests Counters 
	num_of_request_sent = 0
	num_of_request_recived = 0 
	total_request_bytes_sent = 0
	total_request_bytes_recived = 0
	total_request_data_bytes_sent = 0
	total_request_data_bytes_recived = 0

	#ECHO Reply Counters 
	num_of_reply_sent = 0
	num_of_reply_recived = 0
	total_reply_bytes_sent = 0
	total_reply_bytes_recived = 0
	total_reply_data_bytes_sent = 0
	total_reply_data_bytes_recived = 0

	#Constant Frame Size 
	frame_size = 42

	ip_address = ""	

	for node_file in files:
		with open(node_file) as _file:
			if(node_file.split("/")[2] == "Node1_parsed.txt"):
				print("Node 1" + "\n")
				ip_address = "192.168.100.1"

			elif(node_file.split("/")[2] == "Node2_parsed.txt"):
				print("Node 2" + "\n")
				ip_address = "192.168.100.2"

			elif(node_file.split("/")[2] == "Node3_parsed.txt"):
				print("Node 3" + "\n")
				ip_address = "192.168.200.1"

			elif(node_file.split("/")[2] == "Node4_parsed.txt"):
				print("Node 4" + "\n")
				ip_address = "192.168.200.2"

			request_time = []
			request_time2 = []
			reply_time = []
			reply_time2 = []
			total_packet_count = 0
			total_hop_count = 0

			for line in _file:

				total_packet_count += 1
				line = line.strip().split()
				if(line[8] == "request" and line[2] == ip_address):
					num_of_request_sent += 1
					total_request_bytes_sent += int(line[5])
					total_request_data_bytes_sent += (int(line[5]) - frame_size)
					request_time.append([line[0], line[1], line[11].strip("ttl=")])

				elif(line[8] == "request" and line[2] != ip_address):
					num_of_request_recived += 1
					total_request_bytes_recived += int(line[5])
					total_request_data_bytes_recived += (int(line[5]) - frame_size)
					request_time2.append([line[0], line[1]])
					
				elif(line[8] == "reply" and line[2] == ip_address):
					num_of_reply_sent += 1
					total_reply_bytes_sent += int(line[5])
					total_reply_data_bytes_sent += (int(line[5]) - frame_size)
					reply_time2.append([line[14].strip(")"), line[1]])
					
				elif(line[8] == "reply" and line[2] != ip_address):
					num_of_reply_recived += 1
					total_reply_bytes_recived += int(line[5])
					total_reply_data_bytes_recived += (int(line[5]) - frame_size)
					reply_time.append([line[14].strip(")"), line[1], line[11].strip("ttl=")])
			
			#Final Print Statements For the Data Part 
			print("Echo Requests Sent,Echo Requests Received,Echo Replies Sent,Echo Replies Received")
			print(f"{num_of_request_sent},{num_of_request_recived},{num_of_reply_sent},{num_of_reply_recived}")
			print("Echo Request Bytes Sent (bytes),Echo Request Data Sent (bytes)")
			print(f"{total_request_bytes_sent},{total_request_data_bytes_sent}")
			print("Echo Request Bytes Received (bytes),Echo Request Data Received (bytes)")
			print(f"{total_request_bytes_recived},{total_request_data_bytes_recived}")
			compute_RTT(request_time, reply_time, total_request_bytes_sent, num_of_request_sent, num_of_reply_sent, total_request_data_bytes_sent, request_time2, reply_time2)
			

			#ECHO Requests Counters 
			num_of_request_sent = 0
			num_of_request_recived = 0 
			total_request_bytes_sent = 0
			total_request_bytes_recived = 0
			total_request_data_bytes_sent = 0
			total_request_data_bytes_recived = 0

			#ECHO Reply Counters 
			num_of_reply_sent = 0
			num_of_reply_recived = 0
			total_reply_bytes_sent = 0
			total_reply_bytes_recived = 0
			
	#print('called compute function in compute_metrics.py')

# compute()

