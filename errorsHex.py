#CSci 127 Teaching Staff
#October 2017
#A program that converts hex numbers to decimal, but filled with errors...  
Modified by:  Vivian Tang

def convert(s):#function to convert hex to decimal
	#Takes a hex string as input.Returns decimal equivalent.
	total = 0
	for c in s: #using for loop through the hexString
		total = total * 16 #multiply total by 16
		ascii = ord(c)
if ord('0') <= ascii <= ord('9'):
#It's a decimal number, and return it as decimal:
total = total+ascii - ord('0')
elif ord('A') <= ascii <= ord('F'):
#It's a hex number between 10 and 15, convert and return:
total = total + ascii - ord('A') + 10
elif ord('a') <= ascii <= ord('f'):
#Check if they used lower case:
#It's a hex number between 10 and 15, convert and return:
total = total + ascii - ord('a') + 10
else:
#Not a valid number!
return(-1)
return(total)

def main(): #main function
#asking user to enter hex number
hexString = input("Enter a number in hex: ")
#calling function to convert to hex
print("The number in decimal is", convert(hexString))


#Allow script to be run directly:
if __name__ == "__main__":
main() #calling main method
 
