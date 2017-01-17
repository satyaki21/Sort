#!/usr/bin/python
import sys,time

input_array=[]
if (len(sys.argv) < 2 ):
	print ("")
	print ("Please enter list elements as arguments")
	print ("\nExample: ./bubblesort.py <element1> <element2>....<element n>")
	quit()

i=1
while (i < len(sys.argv)):
	input_array.append(int(sys.argv[i]))
	i+=1

def bubblesort(array):
	length=len(array)
	result = True
	global count
	while result:
		result=False
		i=0
		while(i < length -1):
			if (array[i] > array[i+1]):
				tempVar=array[i]
				array[i]=array[i+1]
				array[i+1]=tempVar
				result = True
			i+=1
			count+=1
			print ("sorting" + str(array))
	return array
count=0
time1=time.time()
arrayResult=str(bubblesort(input_array))
print("")
print ("sorted after"+str(count)+ " tries." )
print ("Sorted:" +arrayResult)
print ("---")
print ("Overall Time" +str(time.time()-time1))