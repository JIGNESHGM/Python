# program 25 :

# Define a class, which have a class parameter and have a same instance
# parameter.

# Hints:
# Define a instance parameter, need add it in __init__ method
# You can init a object with construct parameter or set the value later


# Define a class that has a class parameter and an instance parameter.

class MyClass:
    # Class parameter (shared across all instances of the class)
    class_param = "I am a class parameter"

    def __init__(self, instance_param):
        # Instance parameter (unique to each instance of the class)
        self.instance_param = instance_param

# Example usage:
# Create an object of MyClass with an instance parameter
obj1 = MyClass("I am an instance parameter")

# Access the class parameter
print(MyClass.class_param)  # Output: I am a class parameter

# Access the instance parameter
print(obj1.instance_param)  # Output: I am an instance parameter
