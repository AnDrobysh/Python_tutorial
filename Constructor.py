class Horse:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def horse_name(self):
        return f'Horses named {self.name} {self.age} years old'


burka = Horse('Burka', 13)
print(burka.horse_name())
