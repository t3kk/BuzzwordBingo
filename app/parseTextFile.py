import os.path
from random import randint

def getListFromFile(file, size):
   if os.path.isfile(file):
		#return a list of lines
		listFromFile = [line.strip() for line in open(file)]
		return listFromFile
   else:
      #return an empty list
      return list()

def insertBlank(targetList):
  #change the middle element to free spac
	targetList[len(targetList)/2] = 'Free Space'
	return targetList


def getSetListFromFile(file, size):
	listFromFile = getListFromFile(file, size)
	randSet = set()
	if len(listFromFile) != 0:
		while len(randSet) < size:
			x=randint(0,len(listFromFile)-1)
			randSet.add(listFromFile[x])
	return list(randSet)
