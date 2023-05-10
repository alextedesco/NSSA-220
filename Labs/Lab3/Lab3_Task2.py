import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]
list1 = []
list2 = []

def data ():
    if (arg1 == ".\md5_original.txt" or arg1 == "md5_original.txt"):
        file1 = open (arg1, 'r')
        file2 = open (arg2, 'r')
    else:
        file2 = open (arg1, 'r')
        file1 = open (arg2, 'r')
    for line in file1:
        line = line.strip ()
        line = line.split(" ")
        list1.append (line)
    for line in file2:
        line = line.strip ()
        line = line.split(" ")
        list2.append (line)

def main ():
    data ()
    count=0
    affected=0
    while count < len (list1):
        value1= list1[count][0], list1[count][1]
        value2 = list2[count][0], list2[count][1]
        if (value1[1] != value2[1]):
            affected+=1
            print (value1[0] + ": MD5 original = " + value1[1] + ", MD5 new = " + value2[1])
        count+=1
        
main ()