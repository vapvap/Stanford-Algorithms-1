# os for path names
# sys for filename from array of arguments
# re - regular expression
# random - for pseudo random number generator for graph contraction
import os, sys, re, random, copy

#find directory path of the directory containing the file at the real path of file and concatenate it with the relative path to the input resource.
inputfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "/../res/kargerMinCut.txt"
#inputfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "/../res/test1.txt"
#inputfilepath = os.path.dirname(os.path.realpath(sys.argv[0])) + "/sample.txt"

#open input file for reading
input = open(inputfilepath, 'r')

#initialize counter and set to 0
counter = 0

#initialize temp value and set to 0
temp = 0

#initialize list for the input
lines = []

#set temp to the first number
temp = input.readline()

#while temp isn't empty
#remove return and newline characters from temp and append it to the list after casting to an int
#increment coutner
#set temp to empty value in case readline() doesn't return an empty string at end of file
#read the next line from file
while temp != '':
	lines.append(re.sub('\r\n', '', temp))
	counter += 1
	temp = ''
	temp = input.readline()

graph = []

for i in lines:
	graph.append([int(j) for j in i.split()])

def get_edgelist(graph):
	edgelist = []
	for i in xrange(0, len(graph)):
		for j in xrange(1, len(graph[i])):
			if graph[i][0] <= graph[i][j]:
				edgelist.append([graph[i][0], graph[i][j]])
	return edgelist

#deprecated
def remove_edge(graph, edge):
	counter = 0
	num_removed = 0
	while counter < len(graph):
		if graph[counter][0] == edge[0]:
			i = 1
			while i < len(graph[counter]):
				if graph[counter][i] == edge[1]:
					graph[counter].pop(i)
					num_removed += 1
				else:
					i += 1
			if num_removed > 0:
				return True
			else: 
				return False
		counter += 1
	return False

def remove_self_edges(edgelist):
	i = 0
	while i < len(edgelist):
		if edgelist[i][0] == edgelist[i][1]:
			edgelist.pop(i)
		else:
			i += 1

def contract_edge(edgelist, edge):
	if edgelist.count(edge) == 0:
		return False
	vert1 = edge[0]
	vert2 = edge[1]
	i = 0

	for i in xrange(0, len(edgelist)):
		if edgelist[i][0] == vert2:
			edgelist[i][0] = vert1
		if edgelist[i][1] == vert2:
			edgelist[i][1] = vert1
	return True

def get_random_edge(edgelist):
	edge_num = random.randrange(0, len(edgelist)-1)
	return edgelist[edge_num]

#deprecated
def edge_copy(edgelist):
	newlist = []
	for i in xrange(0,len(edgelist)):
		newlist.append([edgelist[i][0], edgelist[i][1]])
	return newlist

edgelist = get_edgelist(graph)	
remove_self_edges(edgelist)

min = 10000
new_min = 10000
j = 0

while j < 100:
	edgelist_j = copy.deepcopy(edgelist)
	for i in xrange(0, len(graph)-2):
		edge = get_random_edge(edgelist_j)
		contract_edge(edgelist_j, edge)
		remove_self_edges(edgelist_j)
		new_min = len(edgelist_j)
		if new_min < min:
			min = new_min
	j += 1

print min	
	
