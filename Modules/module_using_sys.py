import sys

print("The Command Line Arguments are :")

for i in sys.argv:
    print(i)
    
    
print('\n\nThe Python Pathe is', sys.path)

import os

print(os.getcwd)