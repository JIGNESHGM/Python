# No Argument Funcation

def no_arguments():
    print("Hello Jignesh")
    
# Funcation Call
no_arguments()

# Funcation Withe Arguments

def argument_funcation(a,b):
    if a<b:
        print("A is Small of B")
    elif a > b:
        print("B is Grater Then A")
    else:
        print("Bothe Are equal")


# Funcation Call
argument_funcation(10,20)


# Local Veriabel Funcation 

x = 22

def local_veriabel(x):
    print("x value is : {0}".format(x))
    x = 10
    print("New value of x is : {0}".format(x))
    

local_veriabel(x)
print("After Funcation call value of x is : {0}".format(x))

# Global Variabel Declare after 

x = 22

def local_veriabel():
    global x
    print("x value is : {0}".format(x))
    x = 10
    print("New value of x is : {0}".format(x))
    

local_veriabel()
print("After Funcation call value of x is : {0}".format(x))


# Deferents arguments 

def defrent_arguments(name, age = 22):
    print ("name is {0} and age for {1}".format(name,age))
    

defrent_arguments("Jignesh")

# funcation key words

def funcation_key_word(a,b=15,c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
    
funcation_key_word(3,7)
funcation_key_word(25, c=25)
funcation_key_word(c=50,a=100)


#VarArage Peramiters

def total(initital = 5 , *numbers, **keywords):
    count = initital
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
        return count
    
print(total(10,1,2,3,vagitabels=50, frutes=100))


# DocString

def print_max(x,y):
    
    x = int(x)
    y = int(y)
    
    if x> y:
        print(x, 'is max')
    else:
        print(y, 'is max')
        
print_max(3,5)
print(print_max.__doc__)

print(help())