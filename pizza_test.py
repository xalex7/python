from Pizza import *

def main():
    appetizer = Pizza("Pepperoni", 16, 10.50, 10)
    print(appetizer)

    dinner = Pizza("Anchovy & Pineapple", 20, 11.95, 8)
    print(dinner)

    dinner.area_per_slice()

    appetizer.area_per_slice()

    dinner.cost_per_slice()

    appetizer.cost_per_slice()

    dinner.cost_per_square_inch()

    appetizer.cost_per_square_inch()

main()