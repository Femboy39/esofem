from esofem import *
setDev(0)

twinkOut("====Basic Calculator====")
twinkOut("=======Add Only=======")

numberOne = twinkInNum("Number 1> ")
numberTwo = twinkInNum("Number 2> ")

twinkOut(numberOne + numberTwo)
twinkInNoText()
