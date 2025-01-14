class Animals:
    def __init__(self,weight,age):
        self.weight = weight
        self.age = age

    def look(self):
        pass

    def breath(self):
        pass

class Fish(Animals):
    def swim(self):
        pass

class Mammal(Animals):
    def run(self):
        pass

class Bird(Animals):
    def fly(self):
        pass

class Domestic_dog(Mammal):
    def __init__(self,weight,age,breed,coat_color):
        self.breed = breed
        self.coat_color = coat_color
        super().__init__(weight,age)

    def bark(self):
        pass

    def retrive(self):
        pass

    def __repr__(self):
        return f"{self.weight}, {self.age}, {self.breed}, {self.coat_color}"

pejsek = Domestic_dog(30,2,"Ohař","Hnědý")
print(pejsek)

cap = Bird(30,5)



