import re

def wordpattern():
	inputs = 'redbluebluered'
	pattern = 'abba'
	inputs1 = re.match('(.+)(.+)\\2\\1', inputs)
	# = print(re.match('(.+)(.+)\\1\\2', inputs
	pattern1 = re.match('(.+)(.+)\\2\\1', pattern)
	# temp = -1
	# alocation = []
	# atomatch = []

	print(inputs[:len(inputs1.group(1))])
	
	# while True:
	# 	temp = inputs.find(inputs1.group(1), temp + 1)
	# 	if temp == -1:
	# 		break
	# 	alocation.append(temp)
	# 	# if temp > 0:
	# 	# 	temp = temp - len(inputs1.group(1))
	# 	atomatch.append(temp)
	# 	print(temp)
		
	# print(alocation)
	# print(atomatch)

	# temp = -1
	# blocation = []
	# while True:
	# 	temp = inputs.find(inputs1.group(2), temp + 1)
	# 	if temp == -1:
	# 		break
	# 	if temp > 0:
	# 		temp1 = temp - len()
	# 	blocation.append(temp)

	# re.split('',inputs)
	# print(len(inputs))
	# for i in range(len(inputs)):
	# 	print(inputs[:len(inputs1.group(1))])
	# print(blocation)
	# print(alocation)


	# inputs2 = re.match(inputs1.group(1), inputs)

	# inputsSplit1 = re.split(inputs1.group(1), inputs)
	# inputsSplit2 = re.split(inputs1.group(2), inputs)
	# patternsSplit1 = re.split(pattern1.group(1), pattern)
	# patternsSplit2 = re.split(pattern1.group(2), pattern)
	# print(inputs1.group(0))
	# print(inputsSplit1)
	# print(inputsSplit2)
	# print(patternsSplit1)
	# print(patternsSplit2)

	# what = re.search('', inputsSplit1)
	# print(what)


	# print(inputs1)
	# #c = inputs.search(a.group(1))
	# this = compile1.finditer(inputs, inputs1.group(1)).span()

	# for i in this:
	# 	print(i.span())
	
	# temp = []

	# if (re.findall(a,inputs).span(0) == (0, 0+len(a)):
	# 	temp.append('a')
	# elif ():


wordpattern()
