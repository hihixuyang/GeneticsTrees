from reference import *
from config import *
## generation de inputs
def generateInput():
	INPUTS[0] = rand.randint(0,20000)
## function de validation a comparer avec le getvalue
def getAnswer():
	return  INPUTS[0] % 400 == 0 or (INPUTS[0] % 4 == 0 and INPUTS[0] % 100 != 0)

populations = []
POP_SIZE = 100
for i in range(POP_SIZE):
	populations.append([RuleManager.generate(),0])

genCount = 1
totalFitness = 0
while totalFitness < 80000:
	#jeu de test
	totalFitness = 0
	for i in range(1000):
		generateInput()
		for j in range(POP_SIZE):
			if RuleManager.getValue(populations[j][0]) == getAnswer():
				populations[j][1] += 1
				totalFitness += 1
	#sort avec la fitness
	populations.sort(key=lambda colonnes: colonnes[1])
	print("gen : ")
	print(genCount)
	print("totalFitness : ")
	print(totalFitness)
	print("meilleur sentence : " + populations[99][0])
	print("meilleur sentence score : ")
	print(populations[99][1])
	#modification de la population
	populationElite = []
	for i in range(90,100):
		populationElite.append(populations[i][0])
	newPop = RuleManager.reproduct(populationElite)
	for i in range(POP_SIZE): 
		populations[i][0]= newPop[i]
		populations[i][1]= 0
		populations[i][0] = RuleManager.mutate(populations[i][0])



	genCount += 1
	
