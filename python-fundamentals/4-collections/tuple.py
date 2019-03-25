# Tuple

my_tuple = ("hello", 12, "world")
print(my_tuple)

my_tuple[0] # get at index
len(my_tuple)
for item in my_tuple:
  print(item)

new_tuple = my_tuple + (123, 122) # concat tuple
repeated_tuple = new_tuple * 3
nested_tuple = ((122, 123), (123, 443))
print(nested_tuple[0][1])

single_element_tuple = (123,) # using just (123) produces an int rather than a tuple

do_not_have_to_use_parenthesis = 12, "hello" 

def return_a_tuple():
  return 123, 456

bob, dave = return_a_tuple() # unpacking a tuple into 2 vars
print(bob)
print(dave)

create_from_list = tuple([123, 145])

print(123 in create_from_list)
print(145 not in create_from_list)

