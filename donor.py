def main():
    answer = float(input("Enter the amount of contribution: $"))
    if answer >= 10000:
        print("Benefactor")
    elif answer < 10000 and answer >= 1000:
        print("Patron")
    elif answer < 1000 and answer >= 200:
        print("Supporter")
    elif answer < 200 and answer>= 15:
        print("Friends")
    elif answer < 15 and answer >= 0:
        print("Cheapskate!")
    elif answer < 0:
        print("You can't take money from a charity!")

main()