import sys
from statistics import stdev

file_input = sys.argv [1]

L = []

def read_data(file, L):
	f = open(file, 'r')
	start = 0
	lookup='@DATA'
	for num, line in enumerate(f,1):
		if lookup in line:
			start = num
		
	with open(file, 'r') as f:
		count = 0
		for line in f:
			count +=1
			if count > start:
				line = line.strip()
				line = line.split(",")
				L.append (line)

def process_numeric_fields (L, field_number):
	count=0
	temp_list = []
	while count < len(L):
		value = float (L[count][field_number - 1])
		temp_list.append(value)
		count+=1
	avg = average(0, temp_list)
	temp_list.sort()
	std = stdev (temp_list)
	
	return temp_list[0], temp_list[-1], avg, std

def count_iris_types (L):
	setosa=0
	veriscolor=0
	virginica=0
	for i in L:
		if i[4] == "Iris-setosa":
			setosa+=1
		elif i[4] == "Iris-versicolor":
			veriscolor+=1
		elif i[4] == "Iris-virginica":
			virginica+=1
	return setosa, veriscolor, virginica

def average (avg, list):
	'''
	Helper function to calculate the average
	'''
	count=0
	while count < len(list):
			avg = avg + list[count]
			count+=1
	avg = avg / count
	return avg

read_data(file_input, L)
sepal_lengths = process_numeric_fields (L, 1)
print ("Sepal Length: min = " + str(sepal_lengths[0]) + ", max = " + str(sepal_lengths[1]) + ", average = " + str(round(sepal_lengths[2], 2)) + ", standard deviation = " + str (round (sepal_lengths[3], 2)))
sepal_widths = process_numeric_fields (L, 2)
print ("Sepal Width: min = " + str (sepal_widths[0]) + ", max = " + str (sepal_widths[1]) + ", average = " + str(round (sepal_widths[2], 2)) + ", standard deviation = " + str (round (sepal_widths[3], 2)))
petal_lengths = process_numeric_fields (L, 3)
print ("Petal Length: min = " +  str (petal_lengths[0]) +  ", max = " +  str (petal_lengths[1]) +  ", average = " +  str (round (petal_lengths[2], 2)) +  ", standard deviation = " +  str (round (petal_lengths[3], 2)))
petal_widths = process_numeric_fields (L, 4)
print ("Petal Width: min = " +  str (petal_widths[0]) +  ", max = " +  str (petal_widths[1]) +  ", average = " +  str (round (petal_widths[2], 2)) +  ", standard deviation = " +  str (round (petal_widths[3], 2)))
iris_amounts = count_iris_types (L)
print ("Iris Types: Iris Setosa = "  + str (iris_amounts [0]) + " Iris Versicolor = " + str(iris_amounts[1]) +  " Iris Virginica = " + str (iris_amounts [2]))
