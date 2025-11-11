A = input("Enter a set of numbers separated by commas: ")
B = input("Enter another set of numbers separated by commas: ")

set_A = set(map(int, A.split(",")))
set_B = set(map(int, B.split(",")))

union_set = set_A.union(set_B)
print("The union of the two sets is:", union_set)

difference_set = set_A.difference(set_B)
print("The difference of set A from set B is:", difference_set)

intersection_set = set_A.intersection(set_B)
print("The intersection of the two sets is:", intersection_set)

symmetric_difference_set = set_A.symmetric_difference(set_B)
print("The symmetric difference of the two sets is:", symmetric_difference_set)
