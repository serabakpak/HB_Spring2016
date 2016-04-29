


def check_if_prime(test_num):
	# if test_num == 2:
	# 		print test_num,"is a prime number."
			
	for num in range(2, test_num):
		
		if test_num % num == 0:
			print test_num,"is NOT a prime number."
			return
	
	print test_num,"is a prime number."
				


test_num = int(raw_input("Enter an integer to test if it's a prime number: "))
check_if_prime(test_num)


# def is_prime(number):
#    for i in range(2, number):
#        if number % i == 0:
#            return False #not prime
#    return True

# number = int(raw_input("Enter an integer to test if it's a prime number: "))
# print is_prime(number)
