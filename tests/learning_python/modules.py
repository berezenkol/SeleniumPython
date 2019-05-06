"""
https://docs.python.org/3/library/
"""

# BUILT-IN MODULES
# import math
# from math import sqrt  # this is the prefered way, because when we import the whole module, it has lots of functions & requires a lot of memory
from external.car import info_car

# class ModulesDemo():
#     def built_in_function(self):
#         print(math.sqrt(100))
#         print(math.fabs(5.22222))
#         print(sqrt(600))
#
# m = ModulesDemo()          # Create an object/instance of the class
# m.built_in_function()      # Call the method of the class using the object/instance
#_______________________________________________________________________________________________________________________#
#CREATING OF YOUR OWN MODULES
#we can import modules from another files (NOT built-in)
class DemoModules():
    def car_description(self):
        make = 'benz'
        model = '587'

        info_car(self,make,model)




m = DemoModules()
m.car_description()




