# os for path names
# sys for filename from array of arguments
# re - regular expression
import os, sys, re

#find directory path of the directory containing the file at the real path of file and concatenate it with the relative path to the input resource.
inputfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "/../res/IntegerArray.txt"
#inputfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "/../res/sample1.txt"
#inputfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "/../res/100.txt"

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

def comparisons_quicksort(unsorted):
	comparisons = quicksort_sub(unsorted, 0, len(unsorted)-1)
	if comparisons < 0:
		print "An error occurred during quicksort"
	return comparisons

def quicksort_sub(unsorted, min, max):
	if min == max:
		return 0
	elif min > max:
		return 0
	else:
		pivot = pivot_three(unsorted, min, max)
		if pivot != min:
			unsorted[pivot], unsorted[min] = unsorted[min], unsorted[pivot]
			pivot = min
		comparisons = max - min
		j = min + 1
		i = min + 1
		while j <= max:
			if unsorted[min] >= unsorted[j]:
				if j != i:
					unsorted[j], unsorted[i] = unsorted[i], unsorted[j]
				i+=1
				j+=1
			else:
				j+=1
		unsorted[min], unsorted[i-1] = unsorted[i-1], unsorted[pivot]
		pivot = i - 1
		comparisons += (quicksort_sub(unsorted, min, pivot-1) + quicksort_sub(unsorted, pivot+1, max))
		return comparisons

def pivot_one(unsorted, min, max):
	return min

def pivot_two(unsorted, min, max):
	return max
def pivot_three(unsorted, min, max):
	middle = (max+min)/2
	if unsorted[max] >= unsorted[min]:
		if unsorted[middle] >= unsorted[max]:
			return max
		elif unsorted[middle] >= unsorted[min]:
			return middle
		else:
			return min
	elif unsorted[max] >= unsorted[middle]:
		return max
	elif unsorted[min] >= unsorted[middle]:
		return middle
	else:
		return min

comparisons = comparisons_quicksort(unsorted)

print unsorted

print comparisons
