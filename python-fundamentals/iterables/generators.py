def gen123():
  yield 1
  yield 2
  yield 3

result = gen123()
print(type(result))

print(next(result))

for value in gen123():
  print(value)

def gen456():
  print("yield 4")
  yield 4
  print("yield 5")
  yield 5
  print("yield 6")
  yield 6

result2 = gen456()

next(result2)
next(result2)