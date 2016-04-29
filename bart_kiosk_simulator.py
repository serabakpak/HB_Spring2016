# one function called load_card
# Your load_card function should accept 4 arguments:
# the first argument is the number of $1 bills the rider is giving the kiosk to load onto their clipper card
# the second argument is the number of $5 bills the rider is giving the kiosk to load onto their clipper card
# the third argument is the number of $10 bills the rider is giving the kiosk to load onto their clipper card
# the fourth argument is the number of $20 bills the rider is giving the kiosk to load onto their clipper card
# Your load_card function should then return the total monetary amount that was loaded onto the riders clipper card
# Tests
# Call load_card with 0 $1 bills, 0 $5 bills, 0 $10 bills, and 0 $20 bills as arguments and print the output. This should print 0.
# Call load_card with 0 $1 bills, 0 $5 bills, 0 $10 bills, and 9 $20 bills as arguments and print the output. This should print 180.
# Call load_card with 2 $1 bills, 3 $5 bills, 0 $10 bills, and 0 $20 bills as arguments and print the output. This should print 17.
# Call load_card with 3 $1 bills, 1 $5 bill, 1 $10 bill, and 3 $20 bills as arguments and print the output. This should print 78.

# Push to Github
#  After successfully testing your function, create a repository on Github named Bart_Kiosk_Simulator.


def load_card(num_1_bills, num_5_bills, num_10_bills, num_20_bills):
	total_loaded = num_1_bills + (5 * num_5_bills) + (10 * num_10_bills) + (20 * num_20_bills)
	print total_loaded

load_card(0, 0, 0, 0)
load_card(0, 0, 0, 9)
load_card(2, 3, 0, 0)
load_card(3, 1, 1, 3)