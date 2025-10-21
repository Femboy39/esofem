#esofem.py

#Set dev variable
developer_mode = None
def setDev(status):
  global developer_mode
  developer_mode = status

#Check dev funct
def dev(e):
	try:
		if developer_mode:
			twinkOut('error')
			twinkOut(e)
	except:
		return None

#print()
def twinkOut(text):
  print(text)

#int()
def twinkNum(string4num):
	try:
		return int(string4num)
	except Exception as e:
		dev(e)

#hex()
def twinkHex(number):
	try:
		intnum = twinkNum(number)
		return hex(intnum)
	except Exception as e:
		dev(e)

#input('str')
def twinkIn(text):
	try:
		inp = input(text)
		return inp
	except Exception as e:
		dev(e)

#input()
def twinkInNoText():
	try:
		inp = input()
		return inp
	except Exception as e:
		dev(e)

#int(input('str'))
def twinkInNum(text):
	try:
		inp = twinkNum(twinkIn(text))
		return inp
	except Exception as e:
		dev(e)

#int(input())
def twinkInNumNoText():
	try:
		inp = twinkNum(twinkInNoText())
		return inp
	except Exception as e:
		dev(e)

#To make older programs compatable
def twink2hex(number):
	return twinkHex(number)

def twink2num(number):
	return twinkNum(number)