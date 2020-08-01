def print_triangle(side_length):
	if side_length < 1:
		return

	print( "[]"* side_length)
	print_triangle(side_length-1)
	
	 
def main():

	length = int (input("Enter side length : "))
	print_triangle(length)

main()