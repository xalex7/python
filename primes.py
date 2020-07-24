def main():
    answer = int(input("Enter the maximum rage: "))
    for i in range(2, answer):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)
main()

