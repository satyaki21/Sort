from random import randint
Arr=[]
for num in range(0,10):
	randomNumber=randint(0,100)
	Arr.append(randomNumber)
print ("Unsorted Array")
print (Arr)

def merge(Arr):
	if len(Arr) > 1:
		middle=len(Arr) // 2
		leftArr=Arr[:middle]
		rightArr=Arr[middle:]

		merge(leftArr)
		merge(rightArr)

		leftIndex=0
		rightIndex=0
		totalIndex=0

		while (leftIndex < len(leftArr) and rightIndex < len(rightArr)):
			if (leftArr[leftIndex] <= rightArr[rightIndex]):
				Arr[totalIndex] = leftArr[leftIndex]
				leftIndex +=1 
				totalIndex += 1

			else:
				Arr[totalIndex] = rightArr[rightIndex]
				rightIndex += 1
				totalIndex += 1

		while (leftIndex < len(leftArr)):
			Arr[totalIndex] = leftArr[leftIndex]
			leftIndex +=1
			totalIndex += 1

		while (rightIndex < len(rightArr)):
			Arr[totalIndex]=rightArr[rightIndex]
			rightIndex += 1
			totalIndex += 1

merge(Arr)
print (Arr)