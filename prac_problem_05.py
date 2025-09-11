marks = {}

phy = int(input("Enter your physics marks: "))
chem = int(input("Enter your chemistry marks: "))
math = int(input("Enter your math marks: "))
eng = int(input("Enter your english marks: "))
bio = int(input("Enter your biology marks: "))
comp = int(input("Enter your computer marks: "))

upd = [{"physics": phy,
       "chemistry": chem,
        "math": math,
        "english": eng,
        "biology": bio,
        "computer": comp
       }]
marks.update(upd[0])

print(marks)