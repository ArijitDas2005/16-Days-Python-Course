my_list = [1,1,1,1,1]
print(len(my_list))
print(my_list)

class Object:
    pass

my_object=Object()
print(my_object)





class CD:

    def __init__(self,songwriter,title,song):
        self.songwriter= songwriter
        self.title= title
        self.song= song


    def __str__(self):
        return f'Album:{self.title} by {self.songwriter}'

    def __len__(self):
        return self.song

    def __del__(self):
        print('CD has been deleted')


my_cd=CD('HGFSD','UDGH',24)
#print(my_cd)
#print(str(my_cd))


print(my_cd)
print(len(my_cd))



del my_cd
#print(my_cd)