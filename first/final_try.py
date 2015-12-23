#PRACTICUM
workfile = open('input.txt', 'r')  #workfile
string = workfile.read()			# our input expression
k = (int)(string.split(' ')[1])		# k from input
l = (int)(string.split(' ')[2])		# l from input
string = string.split(' ')[0]		# our regular input expression
answer = [[0 for n in range(len(string))] for n in range(len(string))]	# our "stack"
set_help = [0]*len(string)					# our help stack element
alphabet = ['a', 'b', 'c']						# our alphabet
currentStackPosition = 0;						# our current stack position
q = 0;
def error() :									# if error
	print "Not a regular expression!"
	exit()
def aconcat() :#set_x, set_y) :					# concatenation of two last expressions in the stack
	global currentStackPosition		
	global answer
	global set_help
	for i in range(len(string)) :
		for j in range(len(string)) :
			if ((answer[currentStackPosition - 2][i] == answer[currentStackPosition - 1][j] == 1) and (i + j < len(string))) :
				set_help[i+j] = 1
	for i in range(len(string)) :
		answer[currentStackPosition - 1][i] = 0
		answer[currentStackPosition - 2][i] = set_help[i]
		set_help[i] = 0
	currentStackPosition -= 1;
	
def aadd() :#set_x, set_y) :					# addidion of two last expressions in the stack
	global currentStackPosition
	global answer
	global set_help
	for i in range(len(string)) :
		if (answer[currentStackPosition - 1][i] == 1) :
			answer[currentStackPosition - 2][i] = 1
			answer[currentStackPosition - 1][i] = 0
	currentStackPosition -= 1;

def aconcatForAstar() :	# help function for making star for the last expression in the stack
	global set_help
	global currentStackPosition
	global answer
	for i in range(len(string)) :
		for j in range(len(string)) :
			if (set_help[i] == answer[currentStackPosition - 1][j] == 1 and (i + j) < len(string)) :
				answer[currentStackPosition - 1][i + j] = 1;

def astar(l_from_input) :								# making star for the last expression in the stack
	global currentStackPosition
	global answer
	global set_help
	set_help[0] = 1	#star always gives 0
	for i in range(len(string) - 1) :	#filling the same as start expressions
		set_help[i + 1] = answer[currentStackPosition - 1][i + 1]
	for i in range(l_from_input) :
		aconcatForAstar()
	answer[currentStackPosition - 1][0] = 1; #Because star always gives a zero
	for i in range(len(string)) :#cleaning
		set_help[i] = 0
#program BEGGINING
currentStackPosition = 0;
for char in string:
	q += 1 #iterations
	if q == len(string) + 1: 
		break
	if char in alphabet:								# if char
		answer[currentStackPosition][1] = 1;
		currentStackPosition += 1;
	elif char == '1' :									# if epsilon
		answer[currentStackPosition][0] = 1
		currentStackPosition += 1
	elif char == '.' :									# if concatenation
		if currentStackPosition < 2 :
			error()
		aconcat()
	elif char == '+' :									# if addition
		if currentStackPosition < 2 :
			error()
		aadd()
	elif char == '*' :									# if star
		if currentStackPosition < 1 :
			error()
		astar(l)
	else :												# other cases are not possible
		error()
		
for possible_length in range(len(string)) :				#making answer
	if possible_length % k == l and answer[0][possible_length] == 1 :
		print possible_length
		exit(0)
print "INF"
