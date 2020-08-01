def sum_to(n):
	
	if n < 0:
		return "Error: Please enter a positive number"
	
	elif n == 0:
		return 0
		
	elif n <= 1:

		return 1
	return 1/n + sum_to(n-1)



def main():
	n = int (input("Enter value : "))
	print(sum_to(n))


main()

