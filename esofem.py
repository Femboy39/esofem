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
def twinkOut(obj):
  print(obj)

#print fstring
def twinkOutf(obj):
	twinkOut(obj)

#int()
def twinkNum(obj):
	try:
		return int(obj)
	except Exception as e:
		dev(e)

#hex()
def twinkHex(number):
	try:
		return hex(twinkNum(number))
	except Exception as e:
		dev(e)

#input()
def twinkIn(prompt):
	try:
		return input()
	except Exception as e:
		dev(e)

#int(input())
def twinkInNum(prompt):
	try:
		return twinkNum(twinkIn(prompt))
	except Exception as e:
		dev(e)

#len()
def twinkSize(obj):
	try:
		return len(obj)
	except Exception as e:
		dev(e)

#str()
def twinkString(obj2convert):
	try:
		return str(obj2convert)
	except Exception as e:
		dev(e)

#float()
def twinkFloat(obj2convert):
	try:
		return float(obj2convert)
	except Exception as e:
		dev(e)

#type()
def twinkType(obj):
	try:
		return type(obj)
	except Exception as e:
		dev(e)

#dir()
def twinkDir(obj):
	try:
		return dir(obj)
	except Exception as e:
		dev(e)

#max()
def twinkMost(obj):
	try:
		return max(obj)
	except Exception as e:
		dev(e)

#min()
def twinkLeast(obj):
	try:
		return min(obj)
	except Exception as e:
		dev(e)

#obj.upper()
def twinkUp(obj):
	try:
		return obj.upper()
	except Exception as e:
		dev(e)

#obj.lower()
def twinkLow(obj):
	try:
		return obj.lower()
	except Exception as e:
		dev(e)

#round()
def twinkRound(obj):
	try:
		return round(obj)
	except Exception as e:
		dev(e)

#Booleans and other
realTwink = True
notTwink = False
noTwink = None

#To make older programs compatable
def twink2hex(number):
	return twinkHex(number)

def twink2num(number):
	return twinkNum(number)
