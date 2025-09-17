with open("practice.txt","w") as f :
    f.write("I am learning File I/O.\n")
    f.write("using java.\nI like java.")
  

with open ("practice.txt","r") as f:
        data=f.read()

new_data=data.replace("java","python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)  
#file er moddhe jodi kono specific word replace korte chai tahole prothome