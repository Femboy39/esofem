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
		return hex(twinkNum(number))
	except Exception as e:
		dev(e)

#input('str')
def twinkIn(text):
	try:
		return input(text)
	except Exception as e:
		dev(e)

#input()
def twinkInNoText():
	try:
		return input()
	except Exception as e:
		dev(e)

#int(input('str'))
def twinkInNum(text):
	try:
		return twinkIn(twinkNum(text))
	except Exception as e:
		dev(e)

#int(input())
def twinkInNumNoText():
	try:
		return twinkInNoText(twinkNum())
	except Exception as e:
		dev(e)

#To make older programs compatable
def twink2hex(number):
	return twinkHex(number)

def twink2num(number):
	return twinkNum(number)
