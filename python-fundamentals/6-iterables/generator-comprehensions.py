million_squares = ( number*number for number in range(1, 1000001))
list(million_squares)

print(sum(number*number for number in range(1, 1000000)))