from exceptional import convert

print(convert("33"))
# convert("bob") unhandled exception!

def convert_better(value):
  x = -1
  try:
    x = int(value)
  except (ValueError, TypeError) as error:
    print("error {error}".format(error=str(error)))
    pass # empty statement required to make work
  return x

print(convert_better("bob"))

def raising_up(value):
  try:
    return int(value)
  except (ValueError, TypeError) as error:
    print("error {error}".format(error=str(error)))
    raise

def standard_exception(value): 
  try:
    return int(value)
  except:
    raise ValueError()