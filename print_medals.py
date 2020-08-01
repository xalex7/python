def print_medals(countries, counts):
    print("{:>20}{:>7}{:>7}{:>7}".format("Gold","Silver","Bronze","Total")) #Used String <format> from the Python documentation for better alignment;
    for i in range(len(countries)):
        total = counts[i][0] + counts[i][1] + counts[i][2]
        print('{:<13}{:>7}{:>7}{:>7}{:>7}'.format(countries[i],counts[i][0],counts[i][1],counts[i][2], total))

def main():
    countries = ["Canada", "Italy", "Germany", "Japan", "Kazakhstan", "Russia", "South Korea", "United States" ]
    counts = [
                [ 0, 3, 0 ],
                [ 0, 0, 1 ],
                [ 0, 0, 1 ],
                [ 1, 0, 0 ],
                [ 0, 0, 1 ],
                [ 3, 1, 1 ],
                [ 0, 1, 0 ],
                [ 1, 0, 1 ]
            ]
    print_medals(countries, counts)
main()