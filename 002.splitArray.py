# Splitt array of intergers at two parts (left, right). Sum of both arrays must be same.

# Function finds split point
def findSplitPoint(arr, n) : 
	leftSum = 0

	# This is optimal search no nested loops
	# Left sum has been  calculated. 
	# After that we will loop backward to find split point.
	for i in range(0, n) : 
		leftSum += arr[i] 

	rightSum = 0

	# "Backward looping"  and substracting element (loop cursor location at array index) from left sum 
	# and check is it equal (adding that element to right sum at sime time).
	# Take care about "n-1" , -1 last element (backward loopin python). At this way we avoid nested loop (time costly)
	for i in range(n-1, -1, -1) : 
		rightSum += arr[i] 

		leftSum -= arr[i] 

		if (rightSum == leftSum): 
			return i 

	return -1

# Printig two sides of array
def printTwoParts(arr, n) : 
	splitPoint = findSplitPoint(arr, n) 

	if (splitPoint == -1 or splitPoint == n ) : 
		print ("Not Possible") 
		return

	for i in range (0, n) : 
		if(splitPoint == i) : 
			print ("") 
		print (arr[i], end = " ")		 

# Driver Code 
arr = [7,2,5,4,10] 
n = len(arr) 
printTwoParts(arr, n) 
print(" ") 
print("n = {}".format(n))