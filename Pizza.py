from math import *

class Pizza:
    def __init__(self, name, diameter, price, number_of_slices):
        self.__name = name
        self.__diameter = diameter
        self.__price = price
        self.__number_of_slices = number_of_slices
        self.__area = pow((self.__diameter/2), 2) * pi

    def area_per_slice(self):
        print(self.__area / self.__number_of_slices)
    def cost_per_slice(self):
        print(self.__price / self.__number_of_slices)
    def cost_per_square_inch(self):
        print(self.__price / self.__area)

    def __str__(self):
        return f"Your {self.__name} pizza has a diameter of {self.__diameter} inches, a price of ${self.__price}, and {self.__number_of_slices} slices per pie"

