import random as rand
def G(values):
	return values[0] > values[1]
def GE(values):
	return values[0] >= values[1]
def L(values):
	return values[0] < values[1]
def LE(values):
	return values[0] <= values[1]
def NE(values):
	return values[0] != values[1]
def E(values):
	return values[0] == values[1]	
def OR(values):
	return values[0] | values[1]
def AND(values):
	return values[0] & values[1]
def XOR(values):
	return values[0] ^ values[1]
def NOR(values):
	return not (values[0] or values[1])
def NAND(values):
	return not (values[0] and values[1])
def ADD(values):
	return values[0] + values[1]
def SUB(values):
	return values[0] - values[1]
def MUL(values):
	return values[0] * values[1]
def DIV(values):
	if values[1] != 0:
		return values[0] / values[1]
	else:
		return 0
def MOD(values):
	if values[1] != 0:
		return values[0] % values[1]
	else:
		return 0


def INP1(values):
	i = 104
	print(i)
	return i
#[function,inputType,OutputType,arglen,weight]
FUNCTIONS = [[SUB,"num" , "num",2,1],
			 [DIV,"num" , "num",2,1],
			 [MOD,"num" , "num",2,1],
			 [ADD,"num" , "num",2,1],
			 [MUL,"num" , "num",2,1],
			 [XOR,"bin" , "bin",2,1],
			 [OR,"bin" , "bin",2,1],
			 [AND,"bin" , "bin",2,1],
			 [NAND,"bin" , "bin",2,1],
			 [NOR,"bin" , "bin",2,1],
			 [G,"num" , "bin",2,2],
			 [GE,"num" , "bin",2,2],
			 [L,"num" , "bin",2,2],
			 [LE,"num" , "bin",2,2],
			 [NE,"num" , "bin",2,2],
			 [E,"num" , "bin",2,2],
			 [INP1,"null" , "num",0,10]]


