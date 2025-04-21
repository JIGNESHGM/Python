# Veriabel Defind

number =22 

# User Thru Input Get
guess = int(input('Enter Integer Number :- '))

# Chake Number and Guess Number Bothe are same or not 
if number == guess:
    print("Congratulations, you guessed it. \n (but you do not win any prizes!)")
    
    
# Chake guess Number is Less then Number 
elif guess < number:
    print("No, it is a little higher than that")

# Chake guess Number is Grater then Number 
elif guess > number:
    print("No, it is a little lower than that")
    
print("Complet For chaking")



# Chake If True Or Not

if True:
    print("Yes it's True")