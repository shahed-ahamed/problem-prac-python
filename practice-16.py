word ="learning"

with open("practice.txt","r") as f :

    data=f.read()

    if (data.find(word))!=-1:
        print("word found")
    else:
        print("word not found")
