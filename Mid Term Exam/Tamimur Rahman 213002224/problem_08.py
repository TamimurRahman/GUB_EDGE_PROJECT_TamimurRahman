list1 = list(map(int, input("Enter the first list of numbers: ").split()))
list2 = list(map(int, input("Enter the second list of numbers: ").split()))

set1 = set(list1)
set2 = set(list2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Symmetric Difference:", set1 ^ set2)
