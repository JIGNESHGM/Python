class Robot:
    population = 0  # Class variable to keep track of the number of robots
    
    def __init__(self, name):
        self.name = name
        print(f"Initializing {self.name}")
        Robot.population += 1
        
    def __del__(self):
        print(f"Goodbye, {self.name}")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots left.")
            
    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")
        
    def how_many(self):
        print(f"Total robots: {Robot.population}")
        
droidl = Robot("R2-D2")
droidl.say_hi()
droidl.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("Robots can do some work.")

print("Robots have feelings.")

droidl.__del__()
droid2.__del__()
Robot.how_many()