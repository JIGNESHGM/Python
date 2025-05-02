# program 82:

# Please write a program to compress and decompress
# the string "hello world!hello world!hello world!hello world!".

# Hints:
# Use zlib.compress() and zlib.decompress()
# to compress and decompress a string.

import zlib

# Function to compress a string using zlib
def compress_string(input_string):
    # Convert the string to bytes
    byte_string = input_string.encode('utf-8')
    # Compress the byte string
    compressed_data = zlib.compress(byte_string)
    return compressed_data

# Function to decompress a byte string using zlib
def decompress_string(compressed_data):
    # Decompress the byte string
    decompressed_data = zlib.decompress(compressed_data)
    return decompressed_data.decode('utf-8')

# Main function to execute the program
def main():
    input_string = "hello world!hello world!hello world!hello world!"
    print(f"Original string: {input_string}")
    
    # Compress the string
    compressed_data = compress_string(input_string)
    print(f"Compressed data: {compressed_data}")
    
    # Decompress the string
    decompressed_data = decompress_string(compressed_data)
    print(f"Decompressed string: {decompressed_data}")

# Call the main function to run the program
if __name__ == "__main__":
    main()
