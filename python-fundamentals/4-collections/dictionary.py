literal_dictionary = {
  "name": "bob",
  "age": 12 
}
print(literal_dictionary["name"])

list_tuples = [("name", "bob"), ("age", 12)]
my_dictionary = dict(list_tuples)
print(my_dictionary)

other_constructor = dict(name="bob", age=12)

literal_dictionary.update({"name": "bob1", "likes": "jazz"}) # overrides name and adds likes
print(literal_dictionary)

for key in literal_dictionary:
  print("{key} => {value}".format(key=key, value=literal_dictionary[key]))

for value in literal_dictionary.values():
  print("Just value {value}".format(value=value))

for key, value in literal_dictionary.items():
  print("{key} => {value}".format(key=key, value=literal_dictionary[key]))

# Membership is based on keys ONLY
print("name" in literal_dictionary)
print("cat" not in literal_dictionary)

del literal_dictionary["likes"]

complex_dictionary = {
  "bob": [1, 2, 3],
  "dave": [6, 45, 4]
}
from pprint import pprint as pretty_print
print(complex_dictionary)
pretty_print(complex_dictionary)
