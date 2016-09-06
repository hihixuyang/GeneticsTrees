from reference import *
class Rule(object):
	ruleSize = 3
	def __init__(self,value,reference,Input,Output,argl,Weight):
		self.value = value
		self.input = Input 
		self.reference = reference
		self.output = Output
		self.argl = argl
		self.weight = Weight
		self.growPool = [] #le input == le output
		self.totalGrowWeight = 0
		self.mutatePool = [] # input == input  # output == output
		self.totalMutateWeight = 0
		self.swapPool = [] # le output == le output 
		self.totalSwapWeight = 0
	def grow(self):
		sentence = ""
		sentence += self.value
		sentence += "["
		for i in range(0,self.argl):
			roll = rand.randint(0,self.totalGrowWeight)
			for j in self.growPool:
				roll -= j.weight
				if roll <= 0:
					sentence += j.grow()
					break
			
		sentence += "]"
		return sentence




class RuleManager(object):
	rules = []	
	totalRulesWeight = 0
	mutateRate = 1  #%
	def addRule(rule):
		RuleManager.rules.append(rule)
		RuleManager.totalRulesWeight += rule.weight
	def generate():
		#on genere une premiere rule aleatoirement selon le poids
		roll = rand.randint(0,RuleManager.totalRulesWeight)
		for i in RuleManager.rules:
			roll -= i.weight
			if roll <= 0:
				return i.grow()
				break
		
	def initPool():
		for i in RuleManager.rules:
			for j in RuleManager.rules:
				if i.input == j.output and i != j:
					i.growPool.append(j)
					i.totalGrowWeight += j.weight
				if i.input == j.input and i.output == j.output and i != j:
					i.mutatePool.append(j)
					i.totalMutateWeight += j.weight
				if i.output == j.output and i != j:
					i.swapPool.append(j)
					i.totalSwapWeight += j.weight

	def mutate(sentence):
		#pour chaque expression
		expression = ""
		newsentence = sentence
		for i in range(len(sentence)):
			if sentence[i] != "]":
				expression += sentence[i]
			if sentence[i] == "[":
				expression = expression[:-1]
				rule = RuleManager.getRuleByValue(expression)
				
				if rand.randint(1,100) <= RuleManager.mutateRate:
					#si reussit on regarde le type de mutation
					if rand.randint(0,3) <= 2:
						#on change seulement la node
						roll = rand.randint(0,rule.totalMutateWeight)
						for j in rule.mutatePool:
							roll -= j.weight
							if roll <= 0:
								expression = j.value
								break
						#on insert la nouvelle expression dans la sentence
						newsentence = sentence[:-(len(sentence)-(i-3))] 
						newsentence += expression
						newsentence += sentence[i:]
						sentence = newsentence
					else:
						#on supprime et on reconstruit
						roll = rand.randint(0,rule.totalSwapWeight)
						for j in rule.swapPool:
							roll -= j.weight
							if roll <= 0:
								expression = j.value #on change l expression
								rule = RuleManager.getRuleByValue(expression)
								break

						#on insert la nouvelle expression dans la sentence	
						#on trouve ou fini la branche a changer
						startCutIndex = i-3
						compteur = 0;
						while(compteur != -1 ):
							i += 1
							if sentence[i] == "]":
								compteur -= 1
							if sentence[i] == "[":
								compteur += 1
							
						endCutIndex = i+1
						newsentence = sentence[:startCutIndex]#avant le cut
						growSentence = rule.grow()
						newsentence = newsentence + growSentence #on rajoute la nouvelle branche
						newsentence = newsentence + sentence[endCutIndex:]#on rajoute la fin
						sentence = newsentence
						break
				expression = ""
		return sentence
	#prend une sentence et renvoie le tableau de rules de tout les rule de la sentence
	def getRules(sentence):
		rules = []
		expression = ""
		for i in range(len(sentence)):
			if sentence[i] != "]":
				expression += sentence[i]
			if sentence[i] == "[":
				expression = expression[:-1]
				rules.append(RuleManager.getRuleByValue(expression))
				expression = ""
		return rules
	def reproduct(bestSentences):
		sentences = []
		rules = [] #tableau de tous les rules de chaque sentences rules[0][X] 0 etant la sentence X etant la rules
		match = [] # represente un tableau de pair de int qui represente les index des node interchangeable
		for i in bestSentences	:
			rules.append(RuleManager.getRules(i))
		#on trouve toute les node interchangeable
		for i in range(len(rules)): # i = un tableau de rulesmale
			for j in range(len(rules)): # j = un tableau de rulesfemale
				for k in range(len(rules[i])): # k represente un rule des rulesmale
					for l in range(len(rules[j])): # l represente un rule dans rulefemale
						if rules[i][k] in rules[j][l].swapPool: # si la node female est dans les possibilite du male
							match.append([k,l])
				#on choisi un switch entre les 2 index
				if len(match) > 0 :
					matchIndex = rand.randint(0,len(match)-1)
					#on trouve le startIndex et le endIndex de la sentence du match Male
					maleStartIndex = 0;
					maleEndIndex = 0;
					expressionCount = -1;
					for m in range(len(bestSentences[i])):
						if bestSentences[i][m] == "[":
							expressionCount += 1
						if expressionCount  == match[matchIndex][0]:
							maleStartIndex = m-3
							compteur = 0;
							while(compteur != -1 ):
								m += 1
								if bestSentences[i][m] == "]":
									compteur -= 1
								if bestSentences[i][m] == "[":
									compteur += 1
							maleEndIndex = m+1
							break
					#on trouve le startIndex et le endIndex de la sentence du match Female
					femaleStartIndex = 0;
					femaleEndIndex = 0;
					expressionCount = -1;
					for n in range(len(bestSentences[j])):
						if bestSentences[j][n] == "[":
							expressionCount += 1
						if expressionCount == match[matchIndex][1]:
							femaleStartIndex = n-3
							compteur = 0;
							while(compteur != -1 ):
								n += 1
								if bestSentences[j][n] == "]":
									compteur -= 1
								if bestSentences[j][n] == "[":
									compteur += 1
							femaleEndIndex = n+1
							break
					#ON CRE L ENFANT!!!!
					#le debut du male
					newSentence = ""
					newSentence = newSentence + bestSentences[i][:maleStartIndex]
					#on met le segment female
					newSentence = newSentence + bestSentences[j][femaleStartIndex:femaleEndIndex]
					#on rajoute la fin male
					newSentence = newSentence + bestSentences[i][maleEndIndex:]
					sentences.append(newSentence)
				else:
					sentences.append(bestSentences[i])#aucun match possible on renvoit le male
				match.clear()
												

		return sentences
	def getRuleByValue(value):
		for i in RuleManager.rules:
			if i.value == value:
				return i
		return None
	def getValue(sentence):
		expression = sentence[:3]
		sentence = sentence[4:]
		expressions = []
		cutIndex = 0
		compteur = 0
		isNewExpression = False
		for i in range(len(sentence)):
			if sentence[i] == "[":
				compteur += 1
				isNewExpression = True
			elif sentence[i] == "]":
				compteur -= 1

			if compteur == 0 and isNewExpression:
				isNewExpression = False
				expressions.append(sentence[cutIndex:i+1])
				cutIndex = i+1
		
		vals = []
		for i in range(len(expressions)):
			vals.append(RuleManager.getValue(expressions[i]))
		rule = RuleManager.getRuleByValue(expression)
		if rule != None:
			return rule.reference(vals)
		return
		
		
		
		 

##DEFINITION OF RULES
RuleManager.addRule(Rule("xor",XOR,"bin","bin",2,1))
RuleManager.addRule(Rule("_or",OR,"bin","bin",2,1))
RuleManager.addRule(Rule("and",AND,"bin","bin",2,1))
RuleManager.addRule(Rule("nnd",NAND,"bin","bin",2,1))
RuleManager.addRule(Rule("nor",NOR,"bin","bin",2,1))
RuleManager.addRule(Rule("grt",G,"num","bin",2,3))
RuleManager.addRule(Rule("geq",GE,"num","bin",2,3))
RuleManager.addRule(Rule("lsr",L,"num","bin",2,3))
RuleManager.addRule(Rule("leq",LE,"num","bin",2,3))
RuleManager.addRule(Rule("equ",E,"num","bin",2,3))
RuleManager.addRule(Rule("neq",NE,"num","bin",2,3))
RuleManager.addRule(Rule("sub",SUB,"num","num",2,1))
RuleManager.addRule(Rule("add",ADD,"num","num",2,1))
RuleManager.addRule(Rule("mul",MUL,"num","num",2,1))
RuleManager.addRule(Rule("mod",MOD,"num","num",2,1))
RuleManager.addRule(Rule("div",DIV,"num","num",2,1))
RuleManager.addRule(Rule("in1",INP1,"null","num",0,10))
RuleManager.addRule(Rule("in2",INP2,"null","num",0,10))
RuleManager.initPool()

sentence = RuleManager.generate()
sentence1 = RuleManager.generate()
sentence2 = RuleManager.generate()
print(sentence)
print(sentence1)
print(sentence2)
sentences = []
sentences = RuleManager.reproduct([sentence,sentence1,sentence2])
print("new gens")
for i in sentences:
	print(i)

