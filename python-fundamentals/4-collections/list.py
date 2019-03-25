my_list = "show how to index".split(" ")
print(my_list[2]) 
print(my_list[-1]) # last element (1 based)
# Slicing
print(my_list[1: -1]) 
print(my_list[2:]) # everything from position 2
print(my_list[:3]) # everything up to position 3
copy_list = my_list[:] # slice everything to copy list
better_copy = my_list.copy()
another_better_copy = list(my_list)

