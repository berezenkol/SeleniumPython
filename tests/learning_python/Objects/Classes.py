class Fruit(object):
    def __init__(self):
        print('You just created a Fruit class')
    def nutrition(self):
        print('Fruits have lots of vitamins')
    def fruit_shape(self):
        print('All fruits are different')

# f = Fruit()
# f.nutrition()
# f.fruit_shape()

class Apple(Fruit):

    def __init__(self):
        super(Apple,self).__init__()
        print('The new Apple class is defined')

    def nutrition(self):
        super(Apple,self).nutrition()
        print('The nutrition of Apple is....')
    def color(self,size):
        apples = {'small': 'green', 'medium': 'red', 'large': 'yellow'}
        if size in apples:
            print('The color of apple is ' + apples[size])





af = Apple()
af.nutrition()
af.fruit_shape()
af.color('medium')



























# s = 'This is a string'
#
# print(type(s))

#___________________________________________________________________________________________________________________________#
#Creating Classes

# class Car(object):
#     def __init__(self,make,model):
#         self.make = make
#         self.model = model

# now we create an instance (c1 - reference variable that is an instance of the Car Class) of the class outside the Class (it might be another file)

# c1 = Car('bmw', '550i')
# print(c1.make)
# print(c1.model)
#___________________________________________________________________________________________________________________________#
#Creating Methods

#use the previous example
# class Car(object):
#
#     wheels = 4   # member variable
#
#     def __init__(self,make,model):
#         self.make = make
#         self.model = model

    #we create new method to make the code easier

    # def car_info(self):
    #     print('The car make is ' + self.make)
    #     print('The car model is ' + self.model)

# now we create an instance (c1 - reference variable that is an instance of the Car Class) of the class outside the Class (it might be another file)

# c1 = Car('bmw', '550i')
# print(c1.wheels)#-wrong way of use, just an example
# c1.wheels = 3 #-wrong way of use, just an example
# print(c1.wheels)#-wrong way of use, just an example
# c1.car_info()
# print(Car.wheels)   #-that's how we have to use the member variables

#_______________________________________________________________________________________________________________________________#
#Inheritance
# class Car(object):
#     def __init__(self):
#         print('You just created the car instance')
#     def drive(self):
#         print('Car started...')
#     def stop(self):
#         print('Car stopped...')

# c1 = Car()    # - we created the instance of Car Class
# c1.drive()    # - we called the method drive
# c1.stop()     # - we called the method stop

# class BMW(Car):
#     def __init__(self):
#         super(BMW,self).__init__()
#         # Car.__init__(self)
#         print('You just created the BMW instance')
#     def drive(self):                # - overriding the parent's method
#         print('You are driving cool BMW car!')
#         super(BMW,self).drive()    # - if we still want to save the original method from the parent class
#     def headsup_display(self):
#         print('This is a unique BMW feature')
#
# b = BMW()
# b.drive()
# b.stop()
# b.headsup_display()