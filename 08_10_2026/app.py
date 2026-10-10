class Superhero:
    def __init__(self, name, power):
        self.power = power
        self.name=name
    def add_powerlevel(self, other_hero_power):
        return self.power + other_hero_power
