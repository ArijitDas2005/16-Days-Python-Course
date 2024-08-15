class Bird:

    wings= True
    def __init__(self, color, species):
        self.color = color
        self.species= species

my_bird = Bird('black','tucan')
print(my_bird.color)
print(my_bird.species)
print(f"My bird is a {my_bird.species} and it's color is {my_bird.color}.")
print(Bird.wings)




