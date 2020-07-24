def main():
    answer = int(input("How tall the output should be? "))
    for i in range(answer):
        for j in range(i + 1):
            print(" ", end="")
        for k in range(answer - i):
            print("*", end="")
        print()


main()