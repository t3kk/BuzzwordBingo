from random import randint

def syn():
        return "Synergy \n"

def acc():
        return "Accept as Delivered \n"

def rai():
        return "Raise a Defect \n"

#Make a function to call so that we can use it elsewhere as well.
def clarify(clarification):
  x=randint(0,2)

  options = {
       0: syn,
   		1 : acc,
	   	2 : rai,
   }

  return options[x]()

#defin the main class
def main():
  clarification = raw_input("Please Enter Your Clarification: ")
  print clarify(clarification)
