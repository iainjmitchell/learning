from airtravel import *

flight = Flight("AB1234", Aircraft("G-UETP", "Airbus plane", num_rows=22, num_seats_per_row=6))
print(type(flight))
print(flight.number())
print(flight._number)

print(flight.airline())
print(flight.aircraft_model())