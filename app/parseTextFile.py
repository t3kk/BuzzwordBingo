import os.path
from random import randint

def getListFromFile(file, size):
   if os.path.isfile(file):
		#return a list of lines
		list = [line.strip() for line in open(file)]
		if (len(list) != len(set(list)):
			getListFromFile(file, size)
		list = insertBlank(list, size)
		return list
   else:
      #return an empty list
      return list()
	  
def insertBlank(list, size)
	index = int(size/2)
	list[index] = ''
	return list
	

def getSetFromFile(file, size):
	list = getListFromFile(file, size)	
	randSet = set()
	if len(list) != 0:
		while len(randSet) < size:
			x=randint(0,len(list)-1)
			randSet.add(list[x])
	return randSet
