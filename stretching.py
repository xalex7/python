import math

def stretch(array):
    new_array = array.copy() #Since lists in Python are assigned by reference not by value, I made a copy of the original list to maintain it and print it later;
    for i in range(0, len(new_array) * 2, 2):
        split = new_array[i] / 2
        new_array[i] = (math.floor(split)) # this method will round down a float incase of an odd number and it's not effective incase of an even number;
        new_array.insert(i, math.ceil(split))
    return new_array

def main():
    lst1 = [18, 7, 4, 14, 11]
    lst2 = stretch(lst1)
    print(lst1)
    print(lst2)

main()