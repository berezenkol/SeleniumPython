
#     print ('I am at %d' % num)
#     if num > 5:
#         print ('I am above 5')
#     else:
#         print ('I am below 5')
#__________________________________________________________________________________________#
# count = 5
# while count < 10:
#     count = count + 1
#     # count +=1
#     print ('The count is: %s' %count)

#___________________________________________________________________________________________#

# retry = True
# count = 0
#
# while retry:
#     count +=1
#     print('The count is:%s'%count)
#     if count == 5:
#         retry = False


#__________________________________________________________________________________________________#

# counter = 0
# while counter < 15:
#     counter +=1
#     print('The counter is:%s'%counter)
#     if counter == 9:
#         break
#     else:
#         continue

#_______________________________________________________________________________________________________#
#
# my_classses = ['algebra', 'geometry', 'PE', 'science']
#
# for c in my_classses:
#     print (c)
#
#     if c =='PE':
#         print('I got %s'%c)
#         break

#__________________________________________________________________________________________________________#
# my_classses = ['algebra', 'geomtry', 'PE', 'science']
# for c in my_classses:
#     print (c)
#
#     if c == 'PE':
#         continue
#     print('I found:%s'%c)


#_______________________________________________________________________________________________________________#
# Lists#

# cars = ['audi', 'bmw', 'honda']
# print(cars)
# print(cars[1])
# cars.append('toyota')
# print(cars)
#
# cars.extend(['mercedes','lexus'])
# print(cars)
#
# x = cars.count('bmw')
# print(x)
#
# a = len(cars)
# print(a)
#
# cars.insert(2, 'Jeep')
# print(cars)
#
#
#
# b = cars.index('Jeep')
# print(b)
#
# slicing = cars[0:2]
# print(slicing)
#
# print(cars)
# cars.sort()
# print(cars)
#_________________________________________________________________________________________________________________#

#Dictionaries#

# cars_dict = {'make': 'bmw', 'model': '550i', 'year': 20}
# print(cars_dict)
# print(cars_dict['year'])
#
# x = cars_dict.keys()
# print(x)
#
# cars_dict['make']='audi'
# print(cars_dict)
#
# cars_dict['used'] = 'female'
# print(cars_dict)
#
# #Nested Dictionary
#
# d = {'k1':{'nestk1':'nestvalue1', 'nestk2':'nestvalue2'}}
#
# d={"key1": [1, 2, 3], "key2": [4, 5, 6], "key3": [7, 8, 9]}
# print(d["key1"][2])

#___________________________________________________________________________________________________________________#
# real_password = "unsafepassword"
# user_password = input("Enter the password: ")
# while user_password != real_password:
#     user_password = input("Enter the password: ")
#     print("You may enter!")

#___________________________________________________________________________________________________________________#
# clist = ['Canada','USA','Mexico','Australia']
# for x in clist:
#     print(x)
#     if x =='Mexico':
#         break
#_________________________________________________________________________________________________________________________#
# username = (input('Hello, please enter your name '))
# print('Hello, ' + username)
# password = (input('Please enter your password '))
# if password == 'Alice123':
#     print('Welcome ' + username)
# elif password == 'Alice1234':
#     print('This is the correct password too')
# else:
#     print(input('Access denied. Try again '))
#     if password == 'Alice123' or 'Alice1234':
#         print('Finally Welcome ' + username)
#________________________________________________________________________________________________________________________#

# fruits = ['apple','banana','orange']
# a = fruits[0:2]
# print(a)

# for i in fruits:
#     print(i)
#____________________________________________________________________________________________________________________________#

# num = 0
# while num<15:
#     # print('The num is less than 0')
#     num+=1
#     print('The value is %s'%num)
#     if num == 9:
#         break
#_____________________________________________________________________________________________________________________________#
# d = 0
# while d < 10:
#     print('The value od is %s'%d)
#     d+=1
#
#     if d == 8:
#         continue
#     print('This exmple is awesome')
#     print('*'*20)

#______________________________________________________________________________________________________________________________#

# h = 0
#
# while h<20:
#     h += 1
#     print('The value is %s'%h)
#
#     if h == 15:
#         print('The value now is %s'%h)
#         break
# print('No more lines to be executed')


#__________________________________________________________________________________________________#

# slist = ['bmw','audi','benz','jeep','cooper']

# for z in slist:
#     print(z)
#     if z == 'jeep':
#         print('I found %s'%z)
# a = slist[0:3]
# print(a)
#____________________________________________________________________________________________________________#
#COOL FEATURE for FOR LOOPS IN PYTHON ONLY
#ZIP function can handle more than 2 lists

# l1 = ['bmw', 'honda','audi']
# l2 = [2017, 2018, 2019, 2004,2005]
#
# for a,b in zip(l1, l2):
#     print(a)
#     print(b)

#______________________________________________________________________________________________________________#

# range(0,10)
# print(list(range(0,10,3)))

# 1 option:
# l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#
# for number in l:
#     print(number)

# 2 option using range function
# for num in range(1,16):
#     print(num)
#___________________________________________________________________________________________________________#
#METHODS

# def sum_nums():
#     print(3+2)
#
# sum_nums()
#
# def sum_numbers(n1,n2):
#     """
#     Get some of two numbers
#     :param n1:
#     :param n2:
#     :return:
#     """
#     # print(n1+n2)
#     #if we want to save this value and use it somewhere on my code. We assign the method to a variable
#     return n1+n2
#
# sum1 = sum_numbers(6,100)
# print(sum1)
#______________________________________________________________________________________________________________________
#Positional/Optional parameters
# def sum_numbers(n1=7,n2=6):
#     """
#     Get some of two numbers
#     :param n1:
#     :param n2:
#     :return:
#     """
#     # print(n1+n2)
#     #if we want to save this value and use it somewhere on my code. We assign the method to a variable
#     return n1+n2
#
# sum1 = sum_numbers(8,8)
# print(sum1)
#____________________________________________________________________________________________________________________
# def isMetro(city):
#     l = ['sfo','la','was']
#
#     if city in l:
#         return True
#     else:
#         return False
#
# x = isMetro('sfo')
# print(x)
#_____________________________________________________________________________________________________________________#
#Some Built-in Functions
#max()
# def largest_num(*args):
#     print(max(args))
#     #we can also return the value, in this case we save the result in variable which may use further
#     return(max(args))
#
# x = largest_num(-30, -20, -10, 0, 10, 20, 30, 100)
# print(x)
# #min()
# def smallest_num(*args):
#     print(min(args))
#     #we can also return the value, in this case we save the result in variable which may use further
#     return(min(args))
#
# y = smallest_num(-30, -20, -10, 0, 10, 20, 30, 100)
# print(y)
# # abs() - a distance from 0 to choosen argument number
# def abs_function(a):
#     print(abs(a))
#
# abs_function(30)
# abs_function(50)
# # type() - returns the type of item
#
# print(type(99))
# print(type(99.9))
# print(type('abs'))
# listok = ['ki','si','mi']
# print(type(listok))
#___________________________________________________________________________________________________________________#



# def state_net_income(state, gross_income):
#     state_tax = {'CA':0.07,'NY':0.06,'WAS':0.05}
#     #income after federal tax
#     net_income = gross_income-(gross_income*.10)
#     #net income after state tax
#     if state in state_tax:
#         net = net_income-(net_income*state_tax[state])
#         print('Your net income is: %s' % net)
#         # return net
#     else:
#         print('State is not in the list')
#         return None
#
# state_net_income('NY', 100000)

#_________________________________________________________________________________________________________________________#

# animals = ['lion','snake','horse','elefant','crocodile','horse']
# print(type(animals))
# print(animals)
#
# for i in animals:
#     print(i)
#
#     if i == 'elefant':
#         print('I found %s'%i)
#         continue
#______________________________________________________________________________________________________________#
# x = 0
# while x < 15:
#     x += 1
#     print(x)
#     if x == 10:
#         print('The number is %d'%x)
#
#
# x = 22%8
# print(x)

#
def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

f = int(input('Give the number: '))
while f != 1:
    f = collatz(f)

hh = collatz(65)
#_________________________________________________________________________________________________________________#
# from random import randint
#
# def game_any(number):
#
#     if number % 2 == 0:
#         print(number // 2)
#         return number // 2
#     elif number % 2 == 1:
#         result = 3 * number + 1
#         print(result)
#         return result
#
# f = randint(1,30)
# while f != 1:
#     f=game_any(f)

#_________________________________________________________________________________________________________________#
# import random
# messages = ['It is certain',
#             'It is decidedly so',
#             'Yes definitely'
#             'Reply hazy try again',
#             'Ask again later',
#             'Concentrate and ask again',
#             'My reply is no',
#             'Outlook not so good',
#              'Very doubtful']
# print(messages[random.randint(0, len(messages) - 1)])

# spam = ['apples', 'bananas', 'tofu', 'cats']
# spam.insert(3, 'and')
# spam.sort()
# print(spam)


#____________________________________________________________________________________________________________________#
# class SomePractise(object):
#     def __init__(self):
#         pass
#
#     def justpractise(self):
#         h = 0
#         while  h< 20:
#             h += 1
#             print(h)
#             if h == 15:
#                 print('This is %s'%h)
#                 result = print(h*2)
#                 # return result

    # def task(self):
    #     x = int(input('Please enter the number ' ))
    #     if x < 10:
    #         print('Your number is smaller than 10')
    #     elif x > 10:
    #         print('Your number is greater than 10')
# def fruitscolours():
#     fruits = {'apple': 'green', 'banana':'yellow', 'kiwi': 'green'}
#     fruit = input(print('Pease enter your fruit ' ))
#     if fruit in fruits:
#         print('Your fruit is ' + fruits[fruit])




# hh.justpractise()
# hh.task()
# hh = fruitscolours()

# class SomePractise2(SomePractise):
#     def __init__(self):
#         super(SomePractise2,self).__init__()
#
# nn = SomePractise2()
# nn.task()
# nn.justpractise()


#________________________________________________________________________________________________#


# def net_income(state, gross):
#     state_tax = {'CA': 0.07, 'WAS':0.05,'NY': 0.03}
#
#     # net income after federal tax
#     net_after_fed = gross - (gross*0.1)
#
#     #net income after state tax
#
#     if state in state_tax:
#
#         net_after_state = net_after_fed - (net_after_fed * state_tax[state])
#         print(net_after_state)
#         return net_after_state
#
# aa = net_income('CA', 1000)



























