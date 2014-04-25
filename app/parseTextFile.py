import os.path
from random import randint

def getListFromFile(file, size):
   if os.path.isfile(file):
		#return a list of lines
		list = [line.strip() for line in open(file)]
		return list
   else:
      #return an empty list
      return list()

def insertBlank(list):
  #change the middle element to free spac
	list[len(list)/2] = 'Free Space'
	return list


def getSetListFromFile(file, size):
	list = getListFromFile(file, size)
	randSet = set()
	if len(list) != 0:
		while len(randSet) < size:
			x=randint(0,len(list)-1)
			randSet.add(list[x])
	return list(randSet)
