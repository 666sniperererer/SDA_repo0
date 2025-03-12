"""
	1.	Vytvorte triedu Vehicle, ktorá obsahuje nasledujúce vlastnosti:
	•	type (car, motorbike,..)
	•	speed
	•	fuel
	•	properties: list (self driving, gps, etc)
	2.	Implementujte metódu clone(), ktorá vytvorí kópiu inštancie Vehicle.
	3.	Pomocou prototypu vytvorte základné vozidlo a klonujte ho, pričom upravíte jeho vlastnosti (napr. zvýšite rýchlosť alebo zmeníte typ paliva).
	4.  Overte funkcionalitu copy a deepcopy na liste properties
"""

from copy import copy, deepcopy

class Vehicle:
    def __init__(self, vehicle_type: str, speed: float, fuel: str, properties: list[str]):
        self.vehicle_type = vehicle_type
        self.speed = speed
        self.fuel = fuel
        self.properties = properties

    def __str__(self):
        return(f"Vehicle type: {self.vehicle_type}, speed: {self.speed}, fuel: {self.fuel}, properties: {self.properties}")

    def clone_shallow(self):
        return copy(self)

    def clone_deep(self):
        return deepcopy(self)


car_prototype = Vehicle("car",100,"petrol", ["4 seats", "gps", "camera"])
moto_prototype = Vehicle("moto", 150, "petrol", ["1 seat", "no gps", "no camera"])

moto1 = moto_prototype.clone_shallow()
moto2 = moto_prototype.clone_shallow()
car1 = car_prototype.clone_shallow()
car2 = car_prototype.clone_shallow()

moto3 = moto_prototype.clone_deep()
moto4 = moto_prototype.clone_deep()

# vytvorenie zopar aut a motoriek

car1.fuel = "diesel"
moto2.speed = 250


print(f"moto1 {moto1}")
print(f"moto2 {moto2}")
print(f"car1 {car1}")
print(f"car2 {car2}")
print(f"moto3 {moto3}")
print(f"moto4 {moto4}")

moto1.properties.pop()
print(f"moto1 shallowcopy {moto1}")
print(f"moto2 shallowcopy {moto2}")

moto3.properties.pop(0)
print(f"moto3 deepcopy {moto3}")
print(f"moto4 deepcopy {moto4}")

'''
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Enemy(Prototype):
    def __init__(self, name: str, health: float, attack_power: float, items: list):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.items = items

    def clone(self):
        return copy(self)

    def __str__(self):
        return f"Enemy(name={self.name}, health={self.health}, attack_power={self.attack_power})"


base_enemy = Enemy(name="Troll", health=100, attack_power=20)

enemy1 = base_enemy.clone()
enemy2 = base_enemy.clone()

enemy1.name = "Troll Warrior"
enemy2.attack_power = 40

print(enemy1)
print(enemy2)
'''