"""
1. Vytvorte rozhranie Observer (pozorovateľ):
• Deklarujte metódu update(player), ktorá prijme aktuálny stav hráča a vykoná zodpovedajúcu akciu.

2. Vytvorte triedu Player (hráč):
• Obsahuje atribúty health a energy.
• Má metódy na zmenu health a energy.
• Implementuje správu pozorovateľov (add_observer, remove_observer) a notifikáciu pozorovateľov (notify_observers).

3. Vytvorte pozorovateľov (Observers):
• Liečiteľ (Healer): Sleduje zdravie hráča a ak klesne pod 50, automaticky zvýši zdravie o 10 bodov.
• Správca energie (Energy Manager): Sleduje energiu hráča a ak klesne pod 30, zobrazí varovanie.

4. Simulujte zmeny:
• Zmeňte stav hráča (zdravie, energiu) a sledujte, ako pozorovatelia reagujú.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, player):
        pass


class Player:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for obs in self.observers:
            obs.update(self)

    def change_health(self, value):
        self.health += value
        self.notify_observers()

    def change_energy(self, value):
        self.energy += value
        self.notify_observers()


class Healer(Observer):
    def update(self, player):
        if player.health < 50:
            player.change_health(10)
            print(f"Zahojeno, nyní zbývá {player.health} životů.")


class EnergyManager(Observer):
    def update(self, player):
        if player.energy < 30:
            print(f"Dochází mana, woe! Zbývá {player.energy} energie.")


def main():
    player = Player(health=100, energy=100)
    healer = Healer()
    energy_manager = EnergyManager()
    player.add_observer(healer)
    player.add_observer(energy_manager)

    player.change_energy(-80)
    player.change_health(-60)


if __name__ == "__main__":
    main()
