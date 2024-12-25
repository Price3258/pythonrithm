class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'hi i\'m {self.name}')

person_1 = Person("drake")

print(person_1.talk())

person_2 = Person("person1")

print(person_2.talk())

