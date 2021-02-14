file_name = input("Enter the name of the file you'd like to count ")

with open(file_name, 'r') as file:
    words = file.read().split()
    word_count = len(words)
    print(f"There are {word_count} words in your file!")
