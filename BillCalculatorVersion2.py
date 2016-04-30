# Define one function called calculate_bill(). It will calculate the tip amount, the total bill, and a split amount 
# per person all at once! 
# The function will take 3 parameters.
# This time, the only parameter that is required is the initial bill amount. 
# The optional parameter, tip percentage will have a default value of 18.
# Since the bill may not need to be split, make another options parameter with a default value of 1. 
# Since all three things will be calculated at once, you will create three global variables that will hold each of 
# these amounts. (Hint: Initialize them to 0 first.)
# You will reassign the new values to these global variables inside your function. (Hint: Remember the keyword you 
# 	must use to reassign a global variable?)

# Now lets test your fancy new function! 
# This is the example output to print for each of the tests below.
# original bill is 100
# tip amount 18.0
# total bill 118.0
# split amount 118.0

# Call your function by only passing 100 for the bill amount.
# Call your function by passing in 100 for the bill amount and 20 for the tip percentage.
# Call your function by passing in 100 for the bill amount,  25 for the tip percentage, and 3 
#for the number of ways to split the bill.
# Call your function by passing in 100 for the bill amount and 2 for the number of ways to split the bill. 
# Bonus challenge! Create a docstring at the top of your file describing your program.

"""This program is a bill calculator. Just enter in the original amount and it calculates the total 
including the tip. You can also enter the size of your party and the program will split the bill for you!"""


bill_amount = 0
tip_percentage = 0
size_party = 0

def calculate_bill(bill_amount, tip_percentage = 18, size_party = 1):
	
	total_bill = bill_amount + bill_amount * tip_percentage/100
	split_amount = total_bill / size_party
	print ''
	print "The original bill is",bill_amount
	print "Tip amount is",(bill_amount * tip_percentage/100)
	print "The total bill is",total_bill
	print "Split amount is",split_amount
	print ''

calculate_bill(100)
calculate_bill(100, tip_percentage = 20)
calculate_bill(100, tip_percentage = 25, size_party = 3)
calculate_bill(100, size_party = 2)