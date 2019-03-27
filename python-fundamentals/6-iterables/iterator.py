iterable = [1, 2, 3, 4]
iterator = iter(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
  print(next(iterator))
except StopIteration as error:
  print("Error: {error}".format(error=str(error)))