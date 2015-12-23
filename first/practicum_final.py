#PRACTICUM
workfile = open('input.txt', 'r')
string = workfile.read()

k = (int)(string.split(' ')[1])
l = (int)(string.split(' ')[2])
string = string.split(' ')[0]

#answer contains sets of lengths of regular expressions which could
#be built from regular expressions contained in stack
#at the same stack position in answer
answer = []

#setting the alphabet of expression
alphabet = ['a', 'b', 'c']

def error() :
	print "Not a regular expression!"
	exit()

def aconcat(set_x, set_y) :
	z = set({})
	for i in set_x :
		for j in set_y :
			z.add(i + j)
	return z

def aadd(set_x, set_y) :
	for i in set_y :
		set_x.add(i)
	return set_x

def astar(set_x, l_from_input) :
	z = set(set_x)
	z.add(0)
	for i in range(l_from_input) :
		a = aconcat(z, set_x)
		for j in a :
			z.add(j)
	return z

i = 0;
for char in string:
	i += 1
	if i == len(string) + 1: 
		break
	if char in alphabet:
		answer.append(set({1}))
	elif char == '1' :
		answer.append(set({0}))
	elif char == '.' :
		if len(answer) < 2 :
			error()
		answer.append(aconcat(answer.pop(), answer.pop()))
	elif char == '+' :
		if len(answer) < 2 :
			error()
		answer.append(aadd(answer.pop(), answer.pop()))
	elif char == '*' :
		if len(answer) < 1 :
			error()
		answer.append(astar(answer.pop(), l))
	else :
		error()
	
#	print "Answer = ", "char=", char,
	print answer

for possible_length in sorted(answer.pop()) :
	if possible_length % k == l :
		print possible_length
		exit(0)
print "INF"
