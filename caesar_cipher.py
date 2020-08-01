import sys

def encryption(word , shift):

	encrypted = ""

	for i in word:

		if i.islower():
			encrypted=encrypted+chr((ord(i) + shift-97) % 26 + 97) 

		elif i.isupper():
			encrypted=encrypted+chr((ord(i) + shift-65) % 26 + 65)

		else:

			 encrypted=encrypted+i


	return encrypted

def decryption(word , shift):

	decrypted = ""

	for i in word:

		if i.islower():
			decrypted=decrypted+chr((ord(i) - shift-97) % 26 + 97) 

		elif i.isupper():
			decrypted=decrypted+chr((ord(i) - shift-65) % 26 + 65)

		else:

			 decrypted=decrypted+i 


	return decrypted

def main():

	shift = int(sys.argv[1])

	if len(sys.argv)==4: 

		
		input_file = open(sys.argv[2],"r+")
		output_file = open(sys.argv[3],"w")

		word= input_file.read()

		print(word)

		output_file.write(encryption(word,shift))

		
	if len(sys.argv)==5:

		input_file = open(sys.argv[3],"r+")
		output_file = open(sys.argv[4],"w")

		word= input_file.read()

		output_file.write(decryption(word,shift))

main()
















