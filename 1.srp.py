"""
Single Responsibility Principle

Uma classe deve ter somente uma responsabilidade
ou
Uma classe deve ter somente um motivo para mudar
"""

class Animal:
    def __init__(self, name: str):
        self.__name = name
    
    def get_name(self):
        return self.__name

class SalvaAnimal:
    data_base = []
    
    def save(self, animal: Animal):
        self.__animal = animal
        SalvaAnimal.data_base.append(self.__animal)