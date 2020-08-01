def is_palindrome(a_string):
	a_string= a_string.lower()
	length = len(a_string)
	if length <2 :
		return True

	if a_string[0]!= a_string[length-1]:
		return False

	return is_palindrome(a_string[1:length-1])

def main():

	print(is_palindrome("foobar"))
	print(is_palindrome("kayaK"))

main()



