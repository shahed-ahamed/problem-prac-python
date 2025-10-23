Vowels = "aeiouAEIOU"
word = "education"
count=0
for char in word:
    if char in Vowels:
        count += 1
        
       
print(f"The number of vowels in the word '{word}' is: {count}")
