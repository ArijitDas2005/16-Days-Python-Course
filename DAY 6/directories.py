import os

#path= os.getcwd()
# print(path)


#path = 'C:\\Users\\HP\\OneDrive\\Desktop\\Python Course\\DAY 6\\test.txt'
#a= os.path.dirname(path)
#b= os.path.basename(path)
#c= os.path.split(path)
#print(a)
#print(b)
#print(c)


#path= os.makedirs('C:\\Users\\HP\\OneDrive\\Desktop\\Alternate Folder\\usygdf12')
#file=open("another_file.txt")
#print(path)
#print(file.read())

#os.rmdir("C:\\Users\\HP\\OneDrive\\Desktop\\Alternate Folder\\usygdf")











from pathlib import Path

folder= Path("C:/Users/HP/OneDrive/Desktop/Alternate Folder")/'another_file.txt'
file= folder/'another_file.txt'
my_file= open(folder)
print(my_file.read())