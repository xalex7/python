def main():
        answer = input("Enter a Roman number: ")
        def roman_to_arabic(roman_number):
            arabic_number = 0
            for i in range(len(roman_number)):
                if roman_number[i] == 'M':
                    arabic_number += 1000
                if roman_number[i] == 'D':
                    if (roman_number[i - 1]) == 'C':
                        arabic_number += 300 # I used this mechanism so when there is a C before the D, the C value will be deducted twice, once for neutralize the value of C and another time to make it negative;
                    else:
                        arabic_number += 500
                if roman_number[i] == 'C':
                    arabic_number += 100
                if roman_number[i] == 'L':
                    arabic_number += 50
                if roman_number[i] == 'X':
                    if (roman_number[i - 1]) == 'I':
                        arabic_number += 8 # Same mechanism that is used with D
                    else:
                        arabic_number += 10
                if roman_number[i] == 'V':
                    if (roman_number[i - 1]) == 'I':
                        arabic_number += 3 # Same mechanism that is used with D
                    else:
                        arabic_number += 5
                if roman_number[i] == 'I':
                    arabic_number += 1
            return arabic_number
        print(roman_to_arabic(answer))
main()

