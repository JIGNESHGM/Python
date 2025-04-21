#Veriabel Delcaration
number = 22 
running = True

while running:
    guess = int(input("Enter Guess Number : "))
    
    # Chake Number and Guess Number Bothe are same or not 
    if number == guess:
        print("Congratulations, you guessed it. \n (but you do not win any prizes!)")
        running = False
        
    # Chake guess Number is Less then Number 
    elif guess < number:
        print("No, it is a little higher than that")

    # Chake guess Number is Grater then Number 
    elif guess > number:
        print("No, it is a little lower than that")
        
    print("Complet For chaking")
    
else:
    print("While Loop is Over")
    
print("Complet")