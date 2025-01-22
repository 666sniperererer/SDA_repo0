aircrafts = [
    {"model": "Boeing 737", "range_km": 5600, "passenger_capacity": 215},
    {"model": "Airbus A320", "range_km": 6300, "passenger_capacity": 180},
    {"model": "Cessna 172", "range_km": 1280, "passenger_capacity": 4},
    {"model": "Boeing 747", "range_km": 14800, "passenger_capacity": 660},
    {"model": "Airbus A380", "range_km": 15200, "passenger_capacity": 853},
    {"model": "Concorde", "range_km": 7222, "passenger_capacity": 100}
]


long_range_aircrafts = list(filter(lambda x: x["range_km"] > 10000, aircrafts))
print("Letadla s doletem nad 10 000 km:", long_range_aircrafts)

#Získat názvy všech letadel:
aircraft_models = list(map(lambda x: x["model"], aircrafts))
print("Modely letadel:", aircraft_models)


from functools import reduce

total_capacity = reduce(lambda acc, x: acc+x["passenger_capacity"], aircrafts, 0)
print("Celková kapacita všech letadel:", total_capacity)



#Mělo by vyjít:
#Letadla s doletem nad 10 000 km: [{'model': 'Boeing 747', 'range_km': 14800, 'passenger_capacity': 660}, {'model': 'Airbus A380', 'range_km': 15200, 'passenger_capacity': 853}]
#Modely letadel: ['Boeing 737', 'Airbus A320', 'Cessna 172', 'Boeing 747', 'Airbus A380', 'Concorde']
#Celková kapacita všech letadel: 2012