# def spam(devideBy):
#     return 42/devideBy
#
# print(spam(2))
# print(spam(5))
# print(spam(0))   # causes an error

#Errors can be handled with try and except statements.
# The code that could potentially have an error is put in a try clause.
# The program execution moves to the start of a following except clause if an error happens.
# def spam(devideBy):
#     try:
#         return 42 / devideBy
#     except ZeroDivisionError:
#         print('Invalid argument')
#
#
# print(spam(2))
# print(spam(5))
# print(spam(0))
#_____________________________________________________________________________________________________________________#

# def exceptionHandling():
#     try:
#         a = 5
#         b = 5
#         c = 2
#
#         d = (a+b)/c
#         print(d)
#     except ZeroDivisionError:
#         print('The error because of division by zero')
#     except TypeError:
#         print('The error because of the string instead of integer')
#     # else - gonna be executed if there is no exception
#     else:
#         print('Because there was no exception, ELSE block is executed')
#     finally:
#         print('FINALLY block always gonna to be executed')
#
# exceptionHandling()
#_____________________________________________________________________________________________________________#

car = {'make':'bmw','model':'i55','year':2018}
print(type(car))
try:
    print(car['color'])
except KeyError:
    print('There is no key color in car dictionary')
finally:
    print('Just we have only these values:')
    for i in car:
        print(car[i])


































