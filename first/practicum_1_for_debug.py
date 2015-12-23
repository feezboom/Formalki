#PRACTICUM
workfile = open('input.txt', 'r')
string = workfile.read()
k = (int)(string.split(' ')[1])
l = (int)(string.split(' ')[2])
string = string.split(' ')[0]
stack = []
answer = []
i = 0;

#setting the alphabet of expression
alphabet = ['a', 'b', 'c']


def error() :
	print "Not a regular expression!"
	exit()

def concat(x, y) :
	if checkplus(x) :
		x = '(' + x + ')'
	if checkplus(y) :
		y = '(' + y + ')'
	return y + x
def aconcat(x, y) :
	z = set({})
	for i in x :
		for j in y :
			z.add(i + j)
	return z

def add(x, y) :
	return y + ' + ' + x
def aadd(x, y) :
	for i in y :
		x.add(i)
	return x

def star(x) :
	return '(' + x + ")*"
def astar(x, l) :
	z = set(x)
	z.add(0)
	for i in range(l) :
		a = aconcat(z, x)
		for j in a :
			z.add(j)
	return z

#function to prevent extra brackets
def checkplus(string) :
	for i in string :
		if i == '+' :
			return True
	return False

#print string

for char in string:
	i += 1
	if i == len(string) + 1: 
		break
#	print "Step number " + str(i)
	if char in alphabet:
		stack.append(char)
		answer.append(set({1}))
	elif char == '1' :
		stack.append(char)
		answer.append(set({0}))
	elif char == '.' :
		if len(stack) < 2 :
			error()
		stack.append(concat(stack.pop(), stack.pop()))
		answer.append(aconcat(answer.pop(), answer.pop()))
	elif char == '+' :
		if len(stack) < 2 :
			error()
		stack.append(add(stack.pop(), stack.pop()))
		answer.append(aadd(answer.pop(), answer.pop()))
	elif char == '*' :
		if len(stack) < 1 :
			error()
		stack.append(star(stack.pop()))
		answer.append(astar(answer.pop(), l))
	else :
		error()
#	print "Answer = ",
#	print answer
	print "Stack = ",
	print stack

answer = answer.pop()
for f in sorted(answer) :
	if f % k == l :
		print f
		exit(0)
print "INF"
