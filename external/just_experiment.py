

#
# listoffruits = ['banana','kiwi']
#
# choice = input('Please enter a fruit ')
# if choice in listoffruits:
#     print('Good')
# else:
#     print('Bad')


# dict = {'elefant':'grey', 'lion':'yellow','crocodile':'green'}



# while True:
#     print('Please enter your animal and know its color ')
#     animal = input()
#     if animal == '':
#         break
#
#     if animal in dict:
#         print('The color of '+animal + ' is ' + dict[animal])
#     else:
#         print('I dont know such animal')


def collatz(number):

    if number %2 == 0:
        print (number//2)
        return number//2

    elif number % 2  == 1:
        result = 3*number+1
        print(result)
        return result

n = input('Please enter the number')
while n != 1:
    n = collatz(int(n))


# while True:
#     print('Hello dear, enter your name ')
#     name = input()
#     if name == 'Luda':
#         print('Hello dear ' + name)
#         break
#     else:
#         continue
# while True:
#     print('Please enter your password')
#     password = input()
#     if password == '123abc':
#         print('The access granted, '+ name)
#         break
#     else:
#         continue

# def collatz_sequence(number):
#     if number % 2 == 0:
#         result = number//2
#         print(result)
#         return result
#
#     elif number % 2 == 1:
#         result = number * 3 + 1
#         print(result)
#         return result
# n = int(input('Please enter the number'))
#
# while n!=1:
#     n = collatz_sequence(n)
#
#
# aa = collatz_sequence(n)








