# Arithmetic Operators - Perform basic mathematical operations
a = 10
b = 3
print("Addition:", a + b)         # Adds two numbers (10 + 3 = 13)
print("Subtraction:", a - b)      # Subtracts b from a (10 - 3 = 7)
print("Multiplication:", a * b)   # Multiplies two numbers (10 * 3 = 30)
print("Division:", a / b)         # Divides a by b (10 / 3 = 3.333...)
print("Floor Division:", a // b)  # Divides and returns integer (10 // 3 = 3)
print("Modulus:", a % b)          # Returns remainder of division (10 % 3 = 1)
print("Exponentiation:", a ** b)  # Raises a to power of b (10^3 = 1000)

# Assignment Operators - Assign values with operations
a = 5
a += 2  # Equivalent to a = a + 2 (5 + 2 = 7)
print("Add and assign:", a)
a -= 1  # Equivalent to a = a - 1 (7 - 1 = 6)
print("Subtract and assign:", a)
a *= 3  # Equivalent to a = a * 3 (6 * 3 = 18)
print("Multiply and assign:", a)
a /= 2  # Equivalent to a = a / 2 (18 / 2 = 9.0)
print("Divide and assign:", a)
a **= 2 # Equivalent to a = a ** 2 (9.0^2 = 81.0)
print("Exponentiate and assign:", a)
a //= 3 # Equivalent to a = a // 3 (81.0 // 3 = 27.0)
print("Floor divide and assign:", a)
a %= 2  # Equivalent to a = a % 2 (27.0 % 2 = 1.0)
print("Modulus and assign:", a)

# Comparison Operators - Compare values and return True/False
x = 5
y = 10
print("Equal to:", x == y)        # Checks if x equals y (False)
print("Not equal to:", x != y)    # Checks if x not equal to y (True)
print("Greater than:", x > y)     # Checks if x greater than y (False)
print("Less than:", x < y)        # Checks if x less than y (True)
print("Greater than or equal to:", x >= y)  # Checks if x >= y (False)
print("Less than or equal to:", x <= y)     # Checks if x <= y (True)

# Logical Operators - Perform logical operations on boolean values
p = True
q = False
print("AND:", p and q)  # True only if both are True (True AND False = False)
print("OR:", p or q)    # True if at least one is True (True OR False = True)
print("NOT:", not p)    # Inverts the boolean value (not True = False)

# Identity Operators - Compare object identity (memory location)
x = [1, 2, 3]
y = x       # y references the same object as x
z = [1, 2, 3]  # z is a different object with same values
print("Is:", x is y)        # True - same object in memory
print("Is not:", x is not z) # True - different objects despite same values

# Membership Operators - Check if value exists in sequence
my_list = [1, 2, 3]
print("In:", 2 in my_list)        # True - 2 exists in list
print("Not in:", 4 not in my_list) # True - 4 doesn't exist in list

# Bitwise Operators - Perform operations on binary representations
a = 10  # Binary: 00001010
b = 3   # Binary: 00000011
print("Bitwise AND:", a & b)   # 00001010 & 00000011 = 00000010 (2)
print("Bitwise OR:", a | b)    # 00001010 | 00000011 = 00001011 (11)
print("Bitwise XOR:", a ^ b)   # 00001010 ^ 00000011 = 00001001 (9)
print("Bitwise NOT:", ~a)      # Inverts all bits (result depends on number representation)
print("Bitwise left shift:", a << 2)  # Shift bits left by 2: 00101000 (40)
print("Bitwise right shift:", a >> 1) # Shift bits right by 1: 00000101 (5)