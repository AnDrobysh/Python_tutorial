class BigGay:
    def __init__(self, name, dick_length):
        self.name = name
        self.dick_length = dick_length
        self.anus_size = 'big'

    def say(self):
        print(f'I am super gay. My name {self.name} and i have {self.dick_length} cm long cock and my anus is very'
              f' {self.anus_size}')


class SmallGay:
    def __init__(self, name, dick_length):
        self.name = name
        self.dick_length = dick_length
        self.anus_size = 'small'

    def say(self):
        print(f'I am super gay. My name {self.name} and i have {self.dick_length} cm long cock and my anus is very'
              f' {self.anus_size}')


class NormalGay:
    def __init__(self, name, dick_length):
        self.name = name
        self.dick_length = dick_length
        self.anus_size = 'normal'

    def say(self):
        print(f'I am super gay. My name {self.name} and i have {self.dick_length} cm long cock and my anus is very'
              f' {self.anus_size}')


class GayFactory:
    dict = {'big': BigGay,
            'small': SmallGay,
            'normal': NormalGay}

    @staticmethod
    def create(name, dick_length, anus_size):
        gay = GayFactory.dict[anus_size]
        new_gay = gay(name, dick_length)

        return new_gay


ivan, jauhen = GayFactory.create('Ivan', 11, 'big'), GayFactory.create('Jauhen', 12, 'small')

ivan.say()
jauhen.say()
