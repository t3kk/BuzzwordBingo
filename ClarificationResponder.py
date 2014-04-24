from random import randint
clarification = raw_input("Please Enter Your Clarification: ")
x=randint(0,2)

def syn():
        print "Synergy \n"

def acc():
        print "Accept as Delivered \n"

def rai():
        print "Raise a Defect \n"

options = {0 : syn,
		1 : acc,
		2 : rai,
}

options[x]()
