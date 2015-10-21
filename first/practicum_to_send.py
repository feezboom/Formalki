#PRACTICUM
workfile = open('input.txt', 'r')
string = workfile.read()

k = (int)(string.split(' ')[1])
l = (int)(string.split(' ')[2])
string = string.split(' ')[0]

#answer contains sets of numbers which could
#be built from regular expressions contained in stack
answer = []
i = 0;

def error() :
	print "Not a regular expression!"
	exit()

def aconcat(x, y) :
	z = set({})
	for i in x :
		for j in y :
			z.add(i + j)
	return z

def aadd(x, y) :
	for i in y :
		x.add(i)
	return x

def astar(x) :
	z = set(x)
	z.add(0)
	for i in range(3) :
		a = aconcat(z, x)
		for j in a :
			z.add(j)
	return z

for char in string:
	i += 1
	if i == len(string) + 1: 
		break
	if char == 'c' or char == 'a' or char == 'b':
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
		answer.append(astar(answer.pop()))
	else :
		error()

for f in sorted(answer.pop()) :
	if f % k == l :
		print f
		exit(0)
print "INF"

