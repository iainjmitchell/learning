class Animal:
  def say_number_of_legs(self):
    legs = self._number_of_legs()
    print("I have {legs} legs".format(legs=legs))

class Cat(Animal):
  def _number_of_legs(self):
    return 4

class Monkey(Animal):
  def _number_of_legs(self):
    return 2

cat = Cat()
cat.say_number_of_legs()
