from random import randint

def syn():
        print "Synergy \n"

def acc():
        print "Accept as Delivered \n"

def rai():
        print "Raise a Defect \n"

#Make a function to call so that we can use it elsewhere as well.
def clarify(clarification):
  x=randint(0,2)

  options = {
       0: syn,
   		1 : acc,
	   	2 : rai,
   }

  options[x]()

#defin the main class
def main():
  clarification = raw_input("Please Enter Your Clarification: ")
  clarify(clarification)
