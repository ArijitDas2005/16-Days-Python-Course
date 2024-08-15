#class Animal:
#    def __init__(self, age, color):
 #       self.age = age
  #      self.color = color

    #def born(self):
     #   print("This animal has been born.")

    #def Talk(self):
     #   print("This animal makes a sound")

#class Bird(Animal):

 #   def __init__(self,age,color,altd):
  #      super().__init__(age, color)
   #     self.altd=altd
    #def talk(self):
     #   print("chirp")

    #def fly(self,feet):
     #   print(f"This bird flies at {feet} feet high.")


#Parrot = Bird(2, 'green',260)
#print(Parrot.color)
#Parrot.born()
#Parrot.talk()
#Parrot.fly(200)

#print('\n')

#my_animal= Animal(5,'black')










class Father:
    def talk(self):
        print("Hello")

class Mother:
    def laugh(self):
        print('ha ha')

    def talk(self):
        print("How are you?")

#class Child(Father,Mother):
 #   pass

class Child(Mother,Father):
    pass

class Grandchild(Child):
    pass

my_grandchild= Grandchild()
my_grandchild.talk()
my_grandchild.laugh()
print(Grandchild.__mro__)

