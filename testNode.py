from node2 import *



def buildBaseNode(baseNodeType):
	#match possible starting functions
	matchFunctions = []
	for i in range(len(FUNCTIONS)):
		if FUNCTIONS[i][2] == baseNodeType:
			matchFunctions.append(i)

	baseNode = Node(matchFunctions[rand.randint(0,len(matchFunctions)-1)])
	return baseNode

baseNode = buildBaseNode("num")

baseNode.buildUntilComplete()
baseNode.describeUntilComplete()
print(baseNode.getValue())
