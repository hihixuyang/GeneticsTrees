from node2 import *


def duplicateTree(baseNode):
	newNode = Node(baseNode.index)
	for i in range(len(baseNode.childs)):
		newNode.childs.append(duplicateTree(baseNode.childs[i]))
	return newNode
def findCompatibleFemale(nodeFemale,output): #retourne le output
	##jet de fertilite
	if rand.randint(0,5) == 1:
		if FUNCTIONS[nodeFemale.index][2] == output: #regarde compatibility
			return nodeFemale
		else:
			for i in range(len(nodeFemale.childs)):
				findCompatibleFemale(nodeFemale.childs[i],output)	
def merge(node1 , node2):
    ##jet de fertilite
	if rand.randint(0,5) == 1:
		##on parcours la femele a la recherche de cells fertile
		node1 = findCompatibleFemale(node2,FUNCTIONS[node1.index][2])
	else:
		for i in range(len(node1.childs)):
			merge(node1.childs[i],node2)	

def reproduct(eliteNodes):
	#on prend la base node du premier mais avec les childs du deuxieme
	newNodes = []
	for i in range(len(eliteNodes)):
		for j in range(len(eliteNodes)):
			node = duplicateTree(eliteNodes[i]) # COPY DE L ARBRE i
			merge(node,eliteNodes[j])
			newNodes.append(node)
	return newNodes


def mutate(baseNode):

	if 1 == 1:
		print("allo")
		index = baseNode.index
		
		node = buildBaseNode(FUNCTIONS[index][2])
		node.buildUntilComplete()
		baseNode = node
	else:
		for i in range(len(baseNode.childs)):
			mutate(baseNode.childs[i])	

def buildBaseNode(baseNodeType):
	#match possible starting functions
	matchFunctions = []
	for i in range(len(FUNCTIONS)):
		if FUNCTIONS[i][2] == baseNodeType:
			matchFunctions.append(i)

	return Node(matchFunctions[rand.randint(0,len(matchFunctions)-1)])
	






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


node1 = buildBaseNode("bin")
node1.buildUntilComplete()
node2 = buildBaseNode("bin")
node2.buildUntilComplete()

print("node 1")
node1.describeUntilComplete()
print("node 2")
node2.describeUntilComplete()

mutate(node1)
print("node 1 mutated")
node1.describeUntilComplete()


"""
while 1:
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
	average = 0
	for i in range(0,100):
		nodes[i][0] = newNodes[i]
		mutate(nodes[i][0])
		nodes[i][1] = 0
	input()"""



