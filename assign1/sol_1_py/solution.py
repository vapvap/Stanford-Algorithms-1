# os for path names
# sys for filename from array of arguments
# re - regular expression
import os, sys, re

#fine directory path of the directory containing the file at the real path of file and concatenate it with the relative path to the input resource.
inputfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "/../res/IntegerArray.txt"

#open input file for reading
input = open(inputfilepath, 'r')

#initialize counter and set to 0
counter = 0

#initialize temp value and set to 0
temp = 0

#initialize list for the input
unsorted = []

#set temp to the first number
temp = input.readline()

#while temp isn't empty
#remove return and newline characters from temp and append it to the list after casting to an int
#increment coutner
#set temp to empty value in case readline() doesn't return an empty string at end of file
#read the next line from file
while temp != '':
	unsorted.append(int(re.sub('\r\n', '', temp)))
	counter += 1
	temp = ''
	temp = input.readline()

# main merge sort function which returns number of inversions

def inversion_merge_sort(unsorted):
	inversions =  merge_sub(unsorted, 0, len(unsorted)-1)
	if inversions < 0:
		print "An error occurred during merge sort\n"
	return inversions

def merge_sub(unsorted, min, max):
	inversions = 0
	if min == max:
		return inversions
	elif min > max:
		return -1
	else:
		temp = []
		inversions = merge_sub(unsorted, min, min + (max - min)/2)
		inversions += merge_sub(unsorted, min + (max-min)/2 + 1, max)
		left, right = min, min + (max-min)/2 + 1
		while (left <= min + (max-min)/2) and (right <= max):
			if unsorted[left] > unsorted[right]:
				inversions += min + (max-min)/2 + 1 - left
				temp.append(unsorted[right])
				right += 1
			else:
				temp.append(unsorted[left])
				left += 1

		if right > max:
			while left <= min + (max-min)/2:
				temp.append(unsorted[left])
				left += 1

		i = 0
		while i < len(temp):
			unsorted[min+i] = temp[i]
			i += 1
		return inversions
	

print inversion_merge_sort(unsorted)

