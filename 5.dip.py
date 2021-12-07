"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

"""
from abc import ABC

class Stats(ABC):
    def __init__(self, name, hp):
        self.__name = name
        self.__hp = hp

    @property
    def hp(self):
            return self.__hp
        
    @property
    def name(self):
        return self.__name
    
class Player(Stats):
    def __init__(self, stats:Stats):
        self.__name = stats.name
        self.__hp = stats.hp
        self.__speed = 1
        
    @property
    def hp(self):
        return self.__hp

    @property
    def name(self):
        return self.__name

class StatsReporter(Stats):
    def __init__(self, stats: Stats):
        self.stats = stats

    def report(self):
        print(f'Name:{self.stats.name()}')
        print(f'HP:{self.stats.hp()}')
