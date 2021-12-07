"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

"""
from abc import ABC

class Creature(ABC):
    def __init__(self, name, hp):
        self.__name = name
        self.__hp = hp

    @property
    def hp(self):
        return self.__hp
        
    @property
    def name(self):
        return self.__name
    
class Player(Creature):
    def __init__(self, name, hp):
        super().__init__(name, hp)

class StatsReporter:
    def __init__(self):
        pass

    def report(self, creature:Creature):
        if isinstance(creature, Creature):
            print(f'Name: {creature.name}')
            print(f'HP: {creature.hp}')
