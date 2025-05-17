from datetime import datetime as dt
from decimal import Decimal
from random import randint, choice
from custom_module import generate_time_travel_message

date = dt.now().date()
time = dt.now().time()


random_year = randint(2026, 2060)
base_cost = Decimal("20.9955")
cost_multiplier = random_year - date.year
final_cost = Decimal(base_cost) * Decimal(cost_multiplier)
formatted_cost = round(final_cost, 2)


destination_list = ["Mars", "Jupiter", "Venus", "Moon", "Sirius", "Sun", "Pluto", "Saturn", "Uranus", "Neptune", "WASP-193b"]
random_destination = choice(destination_list)


print(generate_time_travel_message(random_year, random_destination, formatted_cost))