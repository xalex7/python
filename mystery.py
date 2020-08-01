def mystery(n):
    if n <= 10:
        return 0
    return mystery(n // 2) + 1

def main():
    print(mystery(20)) #The returned value is 1
main()
# mystery(20) returns 1