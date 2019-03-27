from itertools import islice, count

def is_even(number):
  return number % 2 == 0

evens = islice((number for number in count() if is_even(number)), 200)
executed_evens = list(evens)
print(executed_evens)

print(any([True, False, False]))
print(all([True, False, False]))

print(any(is_even(number) for number in range(3, 10)))

one = [1, 2, 4, 5]
two = [10, 20 , 40, 50]
three = [10, 20 , 40, 50]

for one_item, two_item, three_item in zip(one, two, three):
  print("{one}-{two}-{three}".format(one=one_item, two=two_item, three=three_item))

