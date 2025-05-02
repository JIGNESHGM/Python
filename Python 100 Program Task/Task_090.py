# program 90:

# By using list comprehension, please write a program generate a 3*5*8 3D
# array whose each element is 0.

# Hints:
# Use list comprehension to make an array.

# Function to generate a 3D array with dimensions 3x5x8 filled with zeros
def generate_3d_array(dim1, dim2, dim3):
    # Use list comprehension to create a 3D array filled with zeros
    array = []
    for i in range(dim1):
        layer = []
        for j in range(dim2):
            row = []
            for k in range(dim3):
                row.append(0)
            layer.append(row)
        array.append(layer)
    return array

# Main function to execute the program
def main():
    # Dimensions of the 3D array
    # Prompt the user to enter dimensions for the 3D array
    dim1 = int(input("Enter the first dimension (dim1): "))
    dim2 = int(input("Enter the second dimension (dim2): "))
    dim3 = int(input("Enter the third dimension (dim3): "))
    
    # Generate the 3D array
    array_3d = generate_3d_array(dim1, dim2, dim3)
    
    # Print the generated 3D array
    print("Generated 3D array:")
    for layer in array_3d:
        print(layer)
        print()
        
# Call the main function to run the program
if __name__ == "__main__":
    main()
    