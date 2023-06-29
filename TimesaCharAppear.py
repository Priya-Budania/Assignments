# Count number of times a character appears in the string

string = input("Enter a string: ")
character = input("Enter a character to count its appearance: ")

count = 0
for i in string:
    if i == character:
        count +=1
print(f"The character {character} appears {count} times")