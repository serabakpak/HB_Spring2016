# Requirements
# Create a function named travel_to_destination(fare_price, card_value):
# Use a conditional to determine if you can make your trip by comparing the card_value to the fare_price
# If the card_value has enough money to complete the trip, print 'Welcome aboard, enjoy your trip!''
# If the card_value does not have enough money to complete the trip, print 'You need more money!''

# Tests
# Create a variable named clipper_card to hold the value of your card that will get calculated from load_card.  
# You can also create several Clipper card variables such as clipper_card1 and clipper_card2 if you would like 
# to use a different Clipper card for each test case.   Run the following tests:
# Load your clipper card with 3 $1 bills, 0 $5 bills, 0 $10 bills, and 0 $20.  Attempt to travel from FREMONT_TO_COLMA
# Load your clipper card with 0 $1 bills, 0 $5 bills, 0 $10 bills, and 1 $20.  Attempt to travel from HAYWARD_TO_CONCORD
# Load your clipper card with 1 $1 bills, 1 $5 bills, 0 $10 bills, and  $20.  Attempt to travel from DUBLIN_TO_POWELL
# Load your clipper card with 2 $1 bills,  $5 bills, 1 $10 bills, and  $20.  Attempt to travel from FRUITVALE_TO_UNION_CITY

"""I am practicing entering in a Docstring in my file"""



DUBLIN_TO_POWELL = 6.15
FRUITVALE_TO_UNION_CITY = 3.80
ORINDA_TO_RICHMOND = 3.35
HAYWARD_TO_CONCORD = 5.20
FREMONT_TO_COLMA = 6.60


def load_card(num_1_bills, num_5_bills, num_10_bills, num_20_bills):
	return num_1_bills + (5 * num_5_bills) + (10 * num_10_bills) + (20 * num_20_bills)

def travel_to_destination(fare_price, card_value):
	
	if card_value >= fare_price:
		print "Welcome aboard, enjoy your trip!"
	else:
		print "You need more money!"

travel_to_destination(FREMONT_TO_COLMA, load_card(3, 0, 0, 0))
travel_to_destination(HAYWARD_TO_CONCORD, load_card(0, 0, 0, 1))
travel_to_destination(DUBLIN_TO_POWELL, load_card(1, 1, 0, 0))
travel_to_destination(FRUITVALE_TO_UNION_CITY, load_card(2, 0, 1, 0))

# load_card(0, 0, 0, 0)
# load_card(0, 0, 0, 9)
# load_card(2, 3, 0, 0)
# load_card(3, 1, 1, 3)