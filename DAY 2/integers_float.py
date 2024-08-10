# age=input("tell me ur age: ")
# a = print(age)
# print(type(a))

# num1 = 10
# num2 = 25
# num1 = num2
# print(num1,num2)


billwt = int(input())
tax = 0.18
tip = 0.05
totaltax = tax * billwt
totaltip = tip * billwt
totalbill = billwt + totaltax + totaltip
print("The Tax is {}".format(totaltax))
print("The Tip is {}".format(totaltip))
print("Total Bill With Tax and Tip is {}".format(totalbill))
