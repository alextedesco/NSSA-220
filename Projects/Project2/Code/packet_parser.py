'''
Before you can compute metrics, you
must parse the filtered raw text files
and read packet fields into your tool

You may choose to parse the summary
line text or the hex (bonus points will
be awarded for parsing the hex)

The fields you need will be determined
by the metrics you need to compute

'''

def parse() :

	files = ['../Captures/Node1_filtered.txt', '../Captures/Node2_filtered.txt', '../Captures/Node3_filtered.txt', '../Captures/Node4_filtered.txt']
	count = 1

	for fileName in files:
		with open(fileName) as opFile:
		
			new_file_name  = "../Captures/Node" + str(count) + "_parsed.txt" #Creates the filename of the file we send the data to 
			writeFile = open(new_file_name, "w") 
			
			for line in opFile:
				new_line = line.strip().split(" ")
				if(new_line[0] == "No."): #Gets to the next new packet 
					line = opFile.readline() #Goes to the line where the ICMP Packets are stored 
					new_line = line.strip().split()
					if(new_line[4] == "ICMP"): #Looks to see if this is an ICMP Packet 
						if(new_line[8] == "request" or new_line[8] == "reply"): #Filters only ECHO Requests and Replys 
							writeFile.write(line) #Writes the data to the file we created 
		count += 1	#Increases the count to the next Node 
	# print('called parse function in packet_parser.py')
	writeFile.close()
	
# parse()