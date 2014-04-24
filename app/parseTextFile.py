import os.path

def getListFromFile(file):
   if os.path.isfile(file):
      #return a list of lines
      return [line.strip() for line in open(file)]
   else:
      #return an empty list
      return list()
