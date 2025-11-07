movie1 = input("Enter the name of the first movie: ")
movie2 = input ("Enter your second movie name:")
movie3 = input ("Enter your third movie name:")

movies = [movie1, movie2, movie3]
print(movies)


#_______________________________________________________________________________________________________________________________

# checking that a list contain palidrome or not

list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if (list1 == copy_list1):
    print("The list is palindrome")
else:
    print("The list is not palindrome")

    
