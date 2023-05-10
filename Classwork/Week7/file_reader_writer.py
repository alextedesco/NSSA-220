l = open ('iris.txt', 'r')
file_output = open ('new_iris.txt', 'w')

L = []

for i in l:
	newList = i.split (",")
	L.append (newList)
	length = len(newList) - 1
	num = 0
	while num < length:
		newList[num] = float(newList[num]) * 2
		file_output.write(str(newList[num]) + ",")
		num = num + 1
	file_output.write (newList[-1])


