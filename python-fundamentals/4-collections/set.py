a_set = {1, 2, 3, 4, 6}
empty_set = set()

list_with_duplicates = [1, 1, 2, 3, 567]
duplicates_removed = set(list_with_duplicates)
print(duplicates_removed)

for value in a_set:
  print(value)

1 in a_set
12 not in a_set

a_set.add(10)
a_set.update([1, 2, 202])
a_set.update({90, 80, 70})
a_set.remove(10)
#a_set.remove("absent") # KeyError
a_set.discard("absent") # does not care if absent

a_copy = a_set.copy()

# Set algebra
blue_eyes = {"Olive", "Harry", "Lily", "Jack", "Amy"}
blond_hair = {"Harry", "Jack", "Mia", "Josh", "Amy"}
smell_hcn = {"Harry", "Amy"}
taste_ptc = {"Harry", "Lily", "Amy", "Lola"}
o_blood  = {"Mia", "Josh", "Lily", "Olive"}
b_blood = {"Amy", "Jack"}
a_blood = {"Harry"}
ab_blood = {"Josh", "Lola"}

print(blue_eyes.union(blond_hair)) # in either sets
print(blue_eyes.intersection(blond_hair)) # in both sets
print(blue_eyes.difference(blond_hair)) # those with blue eyes and NOT blond hair
print(blue_eyes.symmetric_difference(blond_hair)) # in one set or the other but not both

print(smell_hcn.issubset(blond_hair)) # all the people in one set exist in another
print(taste_ptc.issuperset(smell_hcn)) # all the people in the second set exist in this one

print(a_blood.isdisjoint(o_blood)) # no members in common between sets



