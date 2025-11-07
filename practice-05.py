nums= [45,67,23,89,12,90]
n = int(input("Enter a num you wanna search:"  ))

for el in nums :
    if el==n :
        print (f"{n} is found")
        break
else :
    print (f"{n} is not found")
#______________________________________________________________________________________________________________________________

