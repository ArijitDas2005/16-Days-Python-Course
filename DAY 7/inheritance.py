#class Animal:
 #   pass
#class Bird(Animal):
 #   pass
#print(Bird.__bases__)
#print(Animal.__subclasses__())




#class Animal:
 #   def born(self):
  #      print("This animal has been born.")

#class Bird(Animal):
 #   pass

#Parrot=Bird()
#Parrot.born()





class Animal:

    def __init__(self,age,color):
        self.age= age
        self.color= color

    def born(self):
        print("This animal has been born.")

class Bird(Animal):
    pass

Parrot=Bird(2,'green')
print(Parrot.color)