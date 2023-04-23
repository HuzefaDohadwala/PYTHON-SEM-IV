list1 = ['x','y','z']
list2 = [lst1*num for lst1 in list1 for num in range(1,4)]
print(list2)

list3 = [lst1*num for num in range(1,4) for lst1 in list1]
print(list3)
