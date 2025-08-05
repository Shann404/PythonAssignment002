# creating empty list called my_list
my_list=[]

# appending values to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print (my_list)

# inserting 15 at second position
my_list.insert(1, 15)
print(my_list)

# extending my_list with another list
other_list=[50,60,70]
my_list.extend(other_list)
print(my_list)

# removing last elent from my_list
my_list.pop()
print(my_list)

# sorting my_list in ascending order
my_list.sort()
print(my_list)

# printing index at value 30
index_30=my_list.index(30)
print(index_30)

