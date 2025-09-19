def check_for_line():
    word = "shahed"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data=f.readline()
            if (word in data):
                print("word found at line no:", line_no )
                return
            line_no += 1
    return -1        
print (check_for_line())
            
check_for_line()