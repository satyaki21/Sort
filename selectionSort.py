from random import randint
import time
array=[]
counter=0
for num in range(0,10):
	randomNumber=randint(0,100)
	array.append(randomNumber)
print (array)

for j in range(len(array)):
	minimum=array[j]
	indexofmin=j
	for i in range(j+1,len(array)):
		if array[i] < minimum:
			minimum=array[i]
			indexofmin=i
	temp = array[j]
	array[j]=minimum
	array[indexofmin]=temp

print (array)