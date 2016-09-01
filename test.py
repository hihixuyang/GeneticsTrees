import random as rand

POP_SIZE = 100
class ArbreDecision(object):
	def __init__(self,functions, inputs):
		self.buildFunctions = functions
		self.inputs = inputs
	#def add_node():

	#def mutate():

	#def reproduct(self,arbre):

class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
    def add_child(self, obj):
        self.children.append(obj)

def if_greater(value1,value2):
	return value1 > value2
def if_greater_equal(value1,value2):
	return value1 >= value2
def if_lower(value1,value2):
	return value1 < value2
def if_lower_equal(value1,value2):
	return value1 <= value2
def if_notequal(value1,value2):
	return value1 != value2
def if_equal(value1,value2):
	return value1 == value2	

#def make_node(function, input1,input2):


function = [if_greater,if_greater_equal,if_lower,if_lower_equal,if_notequal,if_equal]
table = [0,0,0,0,0,0,0,0,0] #0 = empty 1 = X 2 = O


population = []
xor_input = [[1,1],[1,0],[0,1],[0,0]]
xor_output = [0,1,1,0]


for i in range(POP_SIZE):
	population.append([function[rand.randint(0,4)],0])



for i in range(POP_SIZE):
	for j in range(4):
		if(population[i][0](xor_input[j][0],xor_input[j][1]) == xor_output[j]):
			population[i][1] += 1


population.sort(key=lambda colonnes: colonnes[1])
#for i in range(POP_SIZE):	
	#print(population[i])
node1 = Node(5)
if type(node1) == Node:
	print(type(node1.data))