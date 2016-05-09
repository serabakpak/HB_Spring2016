# Youll need these functions.
# Function to add to the shopping list. 
# Dont allow adding something that already exists. Instead return a useful message about what happened. 
# Make sure you account for upper and lower case letters.
# Display the updated shopping list in alphabetical order after an item is added. (Hint: Call the function below that you will write.)

# Function that returns the shopping list in alphabetical order.
# Function to remove an item from the list. 
# Handle the case of trying to remove something that isnt there. Display a useful message.
# Make sure you account for upper and lower case letters.
# Display the updated shopping list in alphabetical order.



# Lets test it out the functions youve defined.

# Add 4 items to your shopping list.
# Try adding an item that is already in the list. 
# Remove an item from the shopping list.
# Try removing an item that is not in the list.

shopping_list = []
def add_to_list(item):
	item = item.lower()
	if item not in shopping_list:
		shopping_list.append(item)
		print "Here is your updated shopping list: ",sort_list()
	else:
		print "The item %s is already in your list." % (item)
	
	  
	
def remove_from_list(item):
	item = item.lower()
	if item in shopping_list:
		shopping_list.remove(item)
		print "Here is your updated shopping list: ",sort_list()
	else:
		print "This item does not exist in your list."


def sort_list():
	shopping_list.sort()
	return shopping_list

add_to_list('MILK')
add_to_list('eggs')
add_to_list('butter')
add_to_list('cookies')
add_to_list('cookies')
remove_from_list('cookies')
remove_from_list('book')


# def main():
	
# 	add_to_list() 
# 	print sort_list()

# shopping_list = []


