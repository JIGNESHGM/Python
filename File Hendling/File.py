def write_to_file(file_name, content):
    """Writes content to a file."""
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"Content written to {file_name}")

def append_to_file(file_name, content):
    """Appends content to a file."""
    with open(file_name, 'a') as file:
        file.write(content)
    print(f"Content appended to {file_name}")

def read_from_file(file_name):
    """Reads content from a file."""
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        print(f"Content of {file_name}:\n{content}")
        return content
    except FileNotFoundError:
        print(f"{file_name} not found.")
        return None

def insert_to_file(file_name, content, line_number):
    """Inserts content at a specific line in the file."""
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        
        # Insert the content at the specified line
        lines.insert(line_number - 1, content + '\n')
        
        with open(file_name, 'w') as file:
            file.writelines(lines)
        
        print(f"Content inserted at line {line_number} in {file_name}")
    except FileNotFoundError:
        print(f"{file_name} not found.")

# Example usage
file_name = "example.txt"

# Writing to the file
write_to_file(file_name, "This is the first line.\n")

# Appending to the file
append_to_file(file_name, "This is the second line.\n")

# Inserting into the file
insert_to_file(file_name, "This is an inserted line.", 2)

# Reading from the file
read_from_file(file_name)