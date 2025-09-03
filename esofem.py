#esofem-main.py

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
def twink2num(string4num):
	try:
		return int(string4num)
	except Exception as e:
		dev(e)

#hex()
def twink2hex(number):
	try:
		intnum = twink2num(number)
		hex(intnum)
	except Exception as e:
		dev(e)
