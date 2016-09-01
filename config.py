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

INPUTS = [0]
def INP1(values):
	return INPUTS[0]
#[function,inputType,OutputType,arglen,weight]
FUNCTIONS = [[SUB,"num" , "num",2,0],
			 [DIV,"num" , "num",2,0],
			 [MOD,"num" , "num",2,5],
			 [ADD,"num" , "num",2,0],
			 [MUL,"num" , "num",2,0],
			 [XOR,"bin" , "bin",2,0],
			 [OR,"bin" , "bin",2,1],
			 [AND,"bin" , "bin",2,1],
			 [NAND,"bin" , "bin",2,1],
			 [NOR,"bin" , "bin",2,1],
			 [G,"num" , "bin",2,0],
			 [GE,"num" , "bin",2,0],
			 [L,"num" , "bin",2,0],
			 [LE,"num" , "bin",2,0],
			 [NE,"num" , "bin",2,6],
			 [E,"num" , "bin",2,6],
			 [INP1,"null" , "num",0,15]]


