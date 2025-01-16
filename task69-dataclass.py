from dataclasses import dataclass

@dataclass
class Letadlo:
    typ : str
    kapacita : int
    dolet : int
    rychlost : int

@dataclass
class Zamestnanec:
    vek : int
    plat : int
    naletano : int

@dataclass
class Aerolinie:
    letadel : int
    zamestnanci : int
    incidenty : int


boeing737 = Letadlo("Boeing 737",250,3500,750) # typ/kapacita/dolet/rychlost
kapitan = Zamestnanec(40,200000,2000) #věk,plat,nalétáno na stroji
smartwings = Aerolinie(30,400,1) #počet letadel, počet zaměstnanců, počet incidentů

print(boeing737)
print(kapitan)
print(smartwings)

@dataclass
class TrainUtils:

    @staticmethod
    def calculate_travel_time(distance, speed):
        if speed <= 0:
            raise InvalidSpeedError
        time = round(float(distance / speed),2)
        print(time)

    @staticmethod
    def calculate_ticket_price(distance, base_price_per_km):
        price = distance*base_price_per_km
        print(f"{price} Kč")

class InvalidSpeedError(Exception):
    def __init__(self):
        message = "Neplatná rychlost!"
        super().__init__(message)

try:
    TrainUtils.calculate_travel_time(500,45)
except InvalidSpeedError as e:
    print(e)

TrainUtils.calculate_ticket_price(1000,4)