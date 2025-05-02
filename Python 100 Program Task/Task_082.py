# program 82:

# Please write a program to compress and decompress
# the string "hello world!hello world!hello world!hello world!".

# Hints:
# Use zlib.compress() and zlib.decompress()
# to compress and decompress a string.

# Function to compress a string using zlib
def compress_string(input_string):
    import zlib
    # Convert the string to bytes
    byte_string = input_string.encode('utf-8')
    # Compress the byte string
    compressed_data = zlib.compress(byte_string)
    return compressed_data

# Main function to execute the program
def main():
    input_string = "hello world!hello world!hello world!hello world!"
    print(f"Original string: {input_string}")
    
    # Compress the string
    compressed_data = compress_string(input_string)
    print(f"Compressed data: {compressed_data}")
    
    # Decompress the string
    decompressed_data = zlib.decompress(compressed_data).decode('utf-8')
    print(f"Decompressed string: {decompressed_data}")
    

# Call the main function to run the program
if __name__ == "__main__":
    main()
