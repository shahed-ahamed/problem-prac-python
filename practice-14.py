#recursion function use kore shob element list a print kora

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def show_list(lst, idx):
    if idx == len(lst):
        return
    print(lst[idx])
    show_list(lst, idx + 1)

show_list(a, 0)