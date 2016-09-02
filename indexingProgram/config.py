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
		self.swapPool = [] # le output == le output 
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
	def addRule(rule):
		RuleManager.rules.append(rule)
		RuleManager.totalRulesWeight += rule.weight
	def generate():
		#on genere une premiere rule aleatoirement selon le poids
		roll = rand.randint(0,RuleManager.totalRulesWeight)
		for i in RuleManager.rules:
			roll -= i.weight
			if roll <= 0:
				generateFromSentence(i.value)
				break
		
	def generateFromSentence(sentence):
		0
	def initPool():
		for i in RuleManager.rules:
			for j in RuleManager.rules:
				if i.input == j.output and i != j:
					i.growPool.append(j)
					i.totalGrowWeight += j.weight
				if i.input == j.input and i.output == j.output and i != j:
					i.mutatePool.append(j)
				if i.output == j.output and i != j:
					i.swapPool.append(j)
		
	def mutate(self,sentence):
		sentence = sentence
	def swap(self,sentence1,sentence2):
		sentence = sentence
	def getValue(sentence):
		value = 0
		return value

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
RuleManager.addRule(Rule("equ",LE,"num","bin",2,3))
RuleManager.addRule(Rule("neq",LE,"num","bin",2,3))
RuleManager.addRule(Rule("sub",SUB,"num","num",2,1))
RuleManager.addRule(Rule("add",ADD,"num","num",2,1))
RuleManager.addRule(Rule("mul",MUL,"num","num",2,1))
RuleManager.addRule(Rule("mod",MOD,"num","num",2,1))
RuleManager.addRule(Rule("div",DIV,"num","num",2,1))
RuleManager.addRule(Rule("in1",INP1,"null","num",0,20))

RuleManager.initPool()
sentence = RuleManager.rules[0].grow()
sentence1 = RuleManager.rules[4].grow()
sentence2 = RuleManager.rules[5].grow()
sentence3 = RuleManager.rules[6].grow()
print("sentence 1 ",sentence)
print("sentence 2 ",sentence1)
print("sentence 3 ",sentence2)
print("sentence 4 ",sentence3)
