print("\nTASK 1\n")

name  = input("Enter your name: ")
age = input("Enter your age: ")
country = input("Enter your country: ")

print(f"My name is {name}, I am {age} years old and I am from {country}.\n")
#-------------------------------------------------------------------------------

print("TASK 2\n")

text = input("Enter a sentence: ")

if "blue" in text:
        print(text.replace("blue","red", 1))

#---------------------------------------------------------------------------------

print("\nTASK 3\n")

word = input("Enter a word: ")
sentence = input("Enter a sentence: ")

if word in sentence:        
    index = sentence.index(word)
    count = sentence.count(word)
    print(f"The {word} is found at index {index} and it appears {count} times in this sentences.\n")

else:
    
    print(f'The word "{word}" was not found.\n')

#------------------------------------------------------------------------------------

print("\nTASK 4\n")

file_name = input("Enter a file name: ")

if file_name.endswith(".txt") and file_name.startswith("file_"):
    print("The file name is valid.")
else:
    print("The file name is invalid.")

#----------------------------------------------------------------------------------

print("\nTASK 5\n")

word_list = input("Enter a list of words: ")

# Split the input string by commas
words = word_list.split(',')

# Join the words using a hyphen as the delimiter
result = '-'.join(words)

print(result)








