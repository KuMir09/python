
t_empty = () # Creating an empty tuple
t_int = (1, 2, 3, 4) # Creating a tuple of integers
print(t_int)
t_mixed = (1, 'hello', 3, 'world') # Creating a mixed data type tuple
print(t_mixed)
t_nested = (1, (2, 3), [4, 5]) # Creating a nested tuple
print(t_nested)



t_single_incorrect = ('Satish') # Incorrect single element tuple
print(type(t_single_incorrect))  # Output: <class 'str'>
t_single_correct = ('Satish',) # Correct single element tuple
print(type(t_single_correct))  # Output: <class 'tuple'>
t_single_correct_alt = 'Satish', # Another way to create a single element tuple
print(type(t_single_correct_alt))  # Output: <class 'tuple'>

# Tuple Operations and Methods
t = (1, 2, 3, 1, 1, 4, 5)
print(t)
length = len(t) # 1. len()
print("Length:", length)
count_of_1 = t.count(1) # 2. count()
print("Count of 1:", count_of_1)
index_of_3 = t.index(3) # 3. index()
print("Index of 3:", index_of_3)
item_exists = 4 in t # 4. in
print("Item exists (4 in tuple):", item_exists)
item_not_exists = 7 not in t # 5. not in
print("Item not exists (7 not in tuple):", item_not_exists)
sorted_tuple = sorted(t) # 6. sorted()
print("Sorted tuple:", sorted_tuple)
max_item = max(t) # 7. max()
print("Max item:", max_item)
min_item = min(t) # 8. min()
print("Min item:", min_item)
sum_of_items = sum(t) # 9. sum()
print("Sum of items:", sum_of_items)