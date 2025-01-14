from dataclasses import dataclass

@dataclass
class Human:
    name : str
    age : int
    height : int

honza = Human("Honza", 39, 184)

print(honza)