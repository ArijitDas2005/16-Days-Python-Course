class Bird:

    wings= True
    def __init__(self, color, species):
        self.color = color
        self.species= species

    def chirp(self):
        print(f'tweet, i am {self.color}.')
    def fly(self,feet):
        print(f"The bird flies {feet} feet high.")

tweetie=Bird('yellow','canary')
tweetie.chirp()
tweetie.fly(200)
