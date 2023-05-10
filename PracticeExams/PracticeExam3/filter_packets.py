def filter() :
	
	#Used to count what node we are getting data from
	count =0 
	
	#List of the files we will be using 
	files = ["../Captures/Node1.txt", "../Captures/Node2.txt", "../Captures/Node3.txt", "../Captures/Node4.txt"]

    
	for fileName in files:
		count += 1
		with open(fileName) as opFile:
			new_file_name  = "../Captures/Node" + str(count) + "_filtered.txt" #Creates the filename of the file we send the data to 
			writeFile = open(new_file_name, "w") 
			for line in opFile:
				
				new_line = line.strip().split(" ")
				if(new_line[0] == "No."):
					heading = line
					line = opFile.readline()
					new_line = line.split()
					if(new_line[4] == "ICMP"):
						if(new_line[8] == "request" or new_line[8] == "reply"):
							writeFile.write(heading)
							notBlank = False
							blankCount = 0
							writeFile.write(line + "\n")
							
							while(notBlank != True):
								line = opFile.readline()
								if(line == "\n" and blankCount == 1):
									notBlank = True
									writeFile.write("\n")
								elif(line == "\n"):
									blankCount = 1
								else:
									writeFile.write(line)

	writeFile.close()
	
	#print('called filter function in filter_packets.py')

# filter()