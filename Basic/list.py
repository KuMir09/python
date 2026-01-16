my_list = [1, 2, 3, 4, 5]
mixed_list = ['apple', 3.14, 42, True]

print("my_list[0]:", my_list[0]) # Assigned index value
print("mixed_list[2]:", mixed_list[2])
my_list[2] = 10 # Mutability
print("Updated my_list:", my_list)

# Append: Adds an item to the end of the list. Extend: Adds all items from another list to the end of the list.
list1 = [1, 2, 3]
list2 = [4, 5]
list1.append(list2)
print(list1)
list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2)
print(list1)

list1 = [1, 2, 3, 4]
del list1[1] # Removes the item at a specific index. 
print(list1)

# List Methods
my_list = [1, 2, 3, 4, 5]
print(my_list)
length = len(my_list) # 1. len()
print("Length:", length)
my_list.append(6) # 2. append()
print("List after append:", my_list)
my_list.insert(2, 2.5) # 3. insert()
print("List after insert:", my_list)
my_list.remove(2) # 4. remove()
print("List after remove:", my_list)
popped_item = my_list.pop(3) # 5. pop()
print("Popped item:", popped_item)
item_exists = 4 in my_list # 6. in
print("Item exists (4 in list):", item_exists)
item_not_exists = 7 not in my_list # 7. not in
print("Item not exists (7 not in list):", item_not_exists)
my_list.reverse() # 8. reverse()
print("List after reverse:", my_list)
sorted_list = sorted(my_list) # 9. sorted()
print("Sorted list:", sorted_list)
sorted_list_desc = sorted(my_list, reverse=True) # 10. sorted() with reverse
print("Sorted list (descending):", sorted_list_desc)


# Without using list comprehension
squares = []
for i in range(10):
    squares.append(i**2)
print(squares)

# Using list comprehension
squares = [i**2 for i in range(10)]
print(squares)

# Example: Doubling values and filtering negative numbers
lst = [1, -10, 20, -20, 10, 20, 50]

# Doubling the values in the list
new_lst = [i * 2 for i in lst]
print(new_lst)

# Filtering the list to exclude negative numbers
new_lst = [i for i in lst if i >= 0]
print(new_lst)

# Creating a list of tuples like (number, square_of_number)
new_lst = [(i, i**2) for i in range(10)]
print(new_lst)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Transposing the matrix without using list comprehension
transposed = []
for i in range(4):  # Iterate over columns
    lst = []
    for row in matrix:  # Iterate over rows
        lst.append(row[i])  # Append the element at the ith column of the current row
    transposed.append(lst)  # Append the new row to the transposed matrix

print(transposed)

# Transposing the matrix using list comprehension
transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)






