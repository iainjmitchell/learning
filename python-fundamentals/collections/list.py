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

this_list = [1, 2]
repeated_list = this_list * 10
print(repeated_list)

stuff = "Hello everyone in the world".split()
index = stuff.index("everyone") # 1
# stuff.index("nothere") # ValueError exception

count = stuff.count("in")
12 in [1, 2, 3, 12]
1 not in [1, 2, 3]

del stuff[2] # remove from list by index
stuff.remove("Hello") # remove by value
# stuff.remove("Bob") # ValueError exception

stuff.insert(3, "bob")

print([1, 2, 3] + [4, 5, 6]) # concat into new list
stuff += ["yo", "boy"] # add to existing list

[1, 2, 3].reverse()
[3, 4, 2].sort()
[92, 2, 3].sort(reverse=True) # desc
["bob", "dave", "Bernard"].sort(key=len) 
# key is callable function to determine index, in this case length function

new_sorted_list = sorted(stuff)
new_reversed_list = reversed(stuff)





