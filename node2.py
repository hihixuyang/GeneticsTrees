from config import *
class Node(object):
	def __init__(self,index):
		self.index = index
		self.childs = []
	def getValue(self):
		vals = []
		for i in self.childs:
			vals.append(i.getValue())
		return FUNCTIONS[self.index][0](vals)

	def buildUntilComplete(self):
		#match possible starting functions
		matchFunctions = []
		totalMatchFunctionsWeight = 0
		for i in range(len(FUNCTIONS)):
			if FUNCTIONS[i][2] == FUNCTIONS[self.index][1]:
				matchFunctions.append(i)
				totalMatchFunctionsWeight += FUNCTIONS[i][4]

		longeur = len(self.childs)
		compteur = 0
		inc = 0
		continu = True

		for i in range(longeur,FUNCTIONS[self.index][3]):#pour tout les enfants
			random = rand.randint(0,totalMatchFunctionsWeight -1)

			continu = True
			while continu:  #tant que compteur est plus petit que randomwieght
				compteur += FUNCTIONS[matchFunctions[inc]] [4]

				if compteur >= random :
					self.childs.append(Node(matchFunctions[inc]))
					compteur = 0
					continu = False
					inc = 0
				else:
					
					inc += 1

		for i in range(len(self.childs)):
			self.childs[i].buildUntilComplete()

	def buildChilds(self):
		#match possible starting functions
		matchFunctions = []
		totalMatchFunctionsWeight = 0
		for i in range(len(FUNCTIONS)):
			if FUNCTIONS[i][2] == FUNCTIONS[self.index][1]:
				matchFunctions.append(i)
				totalMatchFunctionsWeight += FUNCTIONS[i][4]


		longeur = len(self.childs)

		compteur = 0
		inc = 0
		continu = True

		for i in range(longeur,FUNCTIONS[self.index][3]):#pour tout les enfants
			random = rand.randint(0,totalMatchFunctionsWeight -1)

			continu = True
			while continu:  #tant que compteur est plus petit que randomwieght
				compteur += FUNCTIONS[matchFunctions[inc]] [4]

				if compteur >= random :
					self.childs.append(Node(matchFunctions[inc]))
					compteur = 0
					continu = False
					inc = 0
				else:
					inc += 1


	def describe(self):
		print(FUNCTIONS[self.index])
		for i in self.childs:
			print("childs" , FUNCTIONS[i.index])

	def describeUntilComplete(self):
		print(FUNCTIONS[self.index])
		for i in self.childs:
			i.describeUntilComplete()
