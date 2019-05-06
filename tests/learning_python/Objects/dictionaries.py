# birthdays = {'Alice': 'April 24','Ivan': 'September 26','Liudmila':'September 2'}
#
# while True:
#     print('Enter your name:(       )')
#     name = input()
#     if name == '':
#         break
#
#     if name in birthdays:
#         print(birthdays[name] + 'is the birthday of' + name)
#     else:
#         print('There is no data for' + name)
#         print('What is your birhday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthdays are updated')

#________________________________________________________________________________________________________________________________#
#  keys(), values(), and items() methods

# spam = {'color':'red','age':42}
# for value in spam.values():
#     print(value)
# for key in spam.keys():
#     print(key)
# for item in spam.items():
#     print(item)
# for k,v in spam.items():
#     print('Key: ' + k + ' Value: ' + str(v))
#______________________________________________________________________________________________________________________________________#
#The setdefault() Method

spam = {'color':'red','age':42}
spam.setdefault('height',86)
print(spam)


a = 'Hello'
a.rjust(10)
print(a)
