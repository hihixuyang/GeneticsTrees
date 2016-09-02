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

INPUTS = []

def INP1(values):
	return INPUTS[0]