from random import randint
import time
array=[]
counter=0
for num in range(0,10):
	randomNumber=randint(0,100)
	array.append(randomNumber)
print (array)

for i in range(len(array)):
	j=i
	while(j>0 and array[j] < array[j-1]):
		array[j], array[j-1] =array[j-1], array[j]
		j-=1
print (array)

