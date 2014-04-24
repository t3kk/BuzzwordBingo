import os.path
from random import randint

def getListFromFile(file):
   if os.path.isfile(file):
      #return a list of lines
      return [line.strip() for line in open(file)]
   else:
      #return an empty list
      return list()

def getSetFromFile(file, size):
	list = getListFromFile(file)
	randSet = set()
	if len(list) != 0:
		while len(randSet) < size:
			x=randint(0,len(list)-1)
			randSet.add(list[x])
	return randSet