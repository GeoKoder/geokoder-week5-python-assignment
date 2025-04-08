# Base class: Superhero
class Superhero:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health

    def attack(self):
        print(f"{self.name} attacks using {self.power}!")

    def heal(self):
        self.health += 10
        print(f"{self.name} heals and now has {self.health} health.")

    def display_info(self):
        print(f"Name: {self.name}, Power: {self.power}, Health: {self.health}")


# Subclass: FlyingHero inherits from Superhero
class FlyingHero(Superhero):
    def __init__(self, name, power, health, flight_speed):
        super().__init__(name, power, health)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} km/h!")


# Example usage
hero1 = Superhero("ThunderMan", "Electric Shock", 100)
hero2 = FlyingHero("SkyQueen", "Wind Blast", 90, 300)

hero1.display_info()
hero1.attack()
hero1.heal()

print("------")

hero2.display_info()
hero2.attack()
hero2.fly()
