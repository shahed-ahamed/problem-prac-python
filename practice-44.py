punc = " !()-[]{};:'\"\,<>./?@#$%^&*_~"

string = input("Enter something here: ")

empty_string = ""

for i in string:
    if i not in punc:
        empty_string += i
        
        
print("The string without punctuation is:", empty_string)
