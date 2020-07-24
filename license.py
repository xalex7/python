import random 

def main():
    def generate_license(n):
        for i in range(n):
            first_letter = chr(random.randint(65, 90))
            second_letter = chr(random.randint(65, 90))
            third_letter = chr(random.randint(65, 90))
            
            digits = random.randint(100, 999)
            print(f"{digits} {first_letter}{second_letter}{third_letter}") #Printing the function just to make it easy for you to see the result;
    
    generate_license(20)
main()
    