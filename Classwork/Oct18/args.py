import sys

def add_nums (num1, num2, myList):
	myList.append (num1)
	myList.append (num2)
	sum = num1 + num2

	num1=0
	num2=0

	return sum, num1, num2

val1 = float (sys.argv[1])
val2 = float (sys.argv[2])
myList = ["hello", "world"]

print (f"List contents: {myList}")
print (f"Values: {val1} {val2}")
sum, num1 = add_nums (val1, val2. myList)
print (f"List contents: {myList}")
print (f"Values: {val1} {val2}")

# print (f"Sum: {sum}")

# print (f"val1= {val1} val2={val2}")

