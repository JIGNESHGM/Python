# program 86:

# Please write a program to generate all sentences where
# subject is in ["I", "You"] and verb is in ["Play", "Love"]
# and the object is in ["Hockey","Football"].

# Hints:
# Use list[index] notation to get a element from a list.

# Function to generate all sentences based on the given subjects, verbs, and objects
def generate_sentences(subjects, verbs, objects):
    sentences = []
    for subject in subjects:
        for verb in verbs:
            for obj in objects:
                sentences.append(f"{subject} {verb} {obj}.")
    return sentences

# Main function to execute the program
def main():
    subjects = ["I", "You"]
    verbs = ["Play", "Love"]
    objects = ["Hockey", "Football"]
    
    sentences = generate_sentences(subjects, verbs, objects)
    
    # Print all generated sentences
    for sentence in sentences:
        print(sentence)
        
# Call the main function to run the program
if __name__ == "__main__":
    main()