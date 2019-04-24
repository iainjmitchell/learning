print(range(3)) # from 0 to 3
print(range(110, 120)) # from 110 to 120
print(list(range(1, 10, 2))) # step argument

# Do not use range for counters - use enumerate()
stuff = ["Dave", "Cherry", "Owen"]
for index, value in enumerate(stuff):
  print("Index: {index} Value: {value}".format(index=index, value=value))

