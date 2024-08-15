class Cow:

    def __init__(self,name):
        self.name=name

    def talk(self):
        print(self.name + ' moos')


class Sheep:

    def __init__(self,name):
        self.name=name

    def talk(self):
        print(self.name + ' bleats')


cow1= Cow("Bahula")
sheep1= Sheep("Cloud")

cow1.talk()
sheep1.talk()

print('\n')

#OR
animals= [cow1,sheep1]

for animal in animals:
    animal.talk()

print('\n')

#OR
def animal_talks(animal):
    animal.talk()
animal_talks(cow1)
animal_talks(sheep1)


