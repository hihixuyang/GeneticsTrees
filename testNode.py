from node2 import *


def duplicateTree(baseNode):
	newNode = Node(baseNode.index)
	for i in range(len(baseNode.childs)):
		newNode.childs.append(duplicateTree(baseNode.childs[i]))
	return newNode


def reproduct(eliteNodes):
	#on prend la base node du premier mais avec les childs du deuxieme
	newNodes = []
	for i in range(len(eliteNodes)):
		for j in range(len(eliteNodes)):
			node = Node(eliteNodes[i].index)
			if FUNCTIONS[eliteNodes[i].index][1] == FUNCTIONS[eliteNodes[j].index][1]:
				node.childs.append(duplicateTree(eliteNodes[j].childs[0]))
				node.childs.append(duplicateTree(eliteNodes[j].childs[1]))
			newNodes.append(node)
	return newNodes
def mutate(baseNode):
	for i in range(len(baseNode.childs)):
		jet = rand.randint(0,100)
		if jet == 1:
			index = baseNode.childs[i].index
			baseNode.childs[i] = None
			baseNode.childs[i] = buildBaseNode(FUNCTIONS[index][2])
			baseNode.childs[i].buildUntilComplete()
		else:
			mutate(baseNode.childs[i])

def buildBaseNode(baseNodeType):
	#match possible starting functions
	matchFunctions = []
	for i in range(len(FUNCTIONS)):
		if FUNCTIONS[i][2] == baseNodeType:
			matchFunctions.append(i)

	baseNode = Node(matchFunctions[rand.randint(0,len(matchFunctions)-1)])
	return baseNode

## phase d initiation
nodes = []
for i in range(0,100):
	nodes.append([buildBaseNode("bin"),0])
	nodes[i][0].buildUntilComplete()
INPUTS.append(0)
## generation de inputs
def generateInput():
	INPUTS[0] = rand.randint(0,20000)
## function de validation a comparer avec le getvalue
def getAnswer():
	return  INPUTS[0] % 400 == 0 or (INPUTS[0] % 4 == 0 and INPUTS[0] % 100 != 0)

while 1
	for i in range(0,1000):
		generateInput()
		for j in range(0,100):
			if nodes[j][0].getValue() == getAnswer():
				nodes[j][1] += 1

	nodes.sort(key=lambda colonnes: colonnes[1])
	
	print("meilleur sujet:")
	print(nodes[99][1])
	nodes[99][0].describeUntilComplete()

	##changement de population
	##on choisi les meilleurs sujets
	eliteNodes = []
	for i in range(90,100):
		eliteNodes.append(nodes[i][0])
	##on change le tableau pour le nouveau et on le fait mutate
	newNodes = []
	newNodes = reproduct(eliteNodes)
	for i in range(0,100):
		##nodes[i][0] = newNodes[i]
		mutate(nodes[i][0])
		nodes[i][1] = 0
	



