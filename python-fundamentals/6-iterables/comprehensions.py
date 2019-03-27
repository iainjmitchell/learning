words = "I am writing a sentence that is meaningless".split()
list_comprehension = [len(word) for word in words]
print(list_comprehension)

set_comprehension = {len(word) for word in words}
print(set_comprehension)

country_to_capital = {
  "UK": "London",
  "USA": "Washington",
  "France": "Paris"
}

dictionary_comprehension = {capital: country for country, capital in country_to_capital.items()}
print(dictionary_comprehension)

def is_even(number):
  return number % 2 == 0

numbers = range(50)
even_numbers = [number for number in numbers if is_even(number)]
print(even_numbers)

