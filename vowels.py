def main():
    def vowel_count(str):
        vowels_array = [0, 0, 0, 0, 0] 
        for char in str:
            if char in ('A', 'a'):
                vowels_array[0] += 1
            elif char in ('E', 'e'):
                vowels_array[1] += 1
            elif char in ('I', 'i'):
                vowels_array[2] += 1
            elif char in ('O', 'o'):
                vowels_array[3] += 1
            elif char in ('U', 'u'):
                vowels_array[4] += 1
        return vowels_array
    print(vowel_count("I think, therefore I am")) #Printing the function just to make it easy for you to see the result;
main()
