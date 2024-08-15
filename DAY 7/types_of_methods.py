class Bird:

    wings= True
    def __init__(self, color, species):
        self.color = color
        self.species= species

    def chirp(self):
        print(f'tweet, i am {self.color}.')
    def fly(self,feet):
        print(f"The bird flies {feet} feet high.")
        self.chirp()

    def paint_black(self):
        self.color='black'
        print(f"Now the color of the bird is {self.color}")

    @classmethod
    def lay_eggs(cls,number):
        print(f'It lays {number} eggs')
        cls.wings=False
        print(Bird.wings)

    @staticmethod
    def look():
        print("The bird looks")

Bird.look()
print('\n')

Bird.lay_eggs(4)
print('\n')

tweetie=Bird('yellow','canary')

tweetie.paint_black()
print('\n')
tweetie.fly(200)


tweetie.wings= False
print(tweetie.wings)
