# def lowercase(text):
#     print(text.lower())
#
# def uppercase(text):
#     print(text.upper())
#
#
# my_function = uppercase
#
# my_function("Mahabali Hanuman")


def lowercase(text):
    print(text.lower())

def uppercase(text):
    print(text.upper())

def one_function(function):
    return function

one_function(uppercase('Srila Prabhupada'))


# def change_letters(type):
#     def lowercase(text):
#         print(text.lower())
#
#     def uppercase(text):
#         print(text.upper())
#
#     if type == 'upp':
#         return uppercase
#     elif type=='low':
#         return lowercase
#
#
# operation = change_letters('upp')
#
# operation('Krishna')



# def decorator_greeting(function):
#
#     def another_function(word):
#
#         print("Hello")
#         function(word)
#         print('Goodbye')
#
#     return another_function
#
# @decorator_greeting
# def uppercase(text):
#     print(text.upper())
#
# def lowercase(text):
#     print(text.lower())
#
#
# lowercase('Radha Rani')
# uppercase('Radha Rani')
