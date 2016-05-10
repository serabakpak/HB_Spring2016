# Youll be using your existing shopping list project or download the solution from the previous lecture. Well continue adding onto this project over the next few lectures so make sure to update it to your Github or save it somewhere you can access it.

# Add a menu function that prints out the different options. Prompt the user to choose one of the menu options. 
# Example:
# print "0 - Main Menu"
# print "1 - Show current list."
# print "2 - Add an item to your shopping list."
#

# Add a main() function. This is where your core logic will be.
# Call your menu option function. 
# Youll use a while loop so the program continuously runs. (Hint: Refer back to your lecture notes.)
# Inside the while loop will be your logic for the menu choices. (Hint: Youll need if and elif statements.)
# When you are done with the main() function, use the special if-statement that will make your program call main() on startup.

shopping_list = []
def add_to_list():
	item = raw_input('Add an item: (Press 0 to return to the Main Menu) ')
	item = item.lower()
	while item != '0':
		
		if item == '0':
			break		
		elif item not in shopping_list:
			shopping_list.append(item)
			print "Here is your updated shopping list: ",sort_list()
			item = raw_input('Add an item: (0 to return to Main Menu) ')
		else:
			print "The item %s is already in your list." % (item)
			item = raw_input('Add an item: (0 to return to Main Menu) ')
	return shopping_list
	user = menu()
	
def remove_from_list():
	item = raw_input('Remove an item: (Press 0 to return to the Main Menu) ')
	item = item.lower()
	while item != '0':
		if item == '0':
			break
		if item in shopping_list:
			shopping_list.remove(item)
			print "Here is your updated shopping list: ",sort_list()
			item = raw_input('Remove an item: (Press 0 to return to the Main Menu) ')
		else:
			print "This item does not exist in your list. Your list is: ",sort_list()
			item = raw_input('Remove an item: (Press 0 to return to the Main Menu) ')
	return shopping_list
	user = menu()

def sort_list():
	shopping_list.sort()
	return shopping_list

def menu():
	user = int(raw_input('\nWelcome to your Shopping List\n\n0 - Main Menu\n1 - Show current list\n2 - Add an item to your shopping list\n3 - Remove an item from your shopping list\n4 - QUIT\n'))
	return user

def main():
 	user = menu()
 	while True:
 		
 		if user == 0:
 			user = menu()
 		elif user == 1:
 			if shopping_list == []:
 				print "\nYour list is empty! Press 2 to add items!"
 				user = menu()
 			else:
				print "\n",sort_list()
			user = menu()
 		elif user == 2:
 			add_to_list()
 			user = menu()
 		elif user == 3:
 			remove_from_list()
 			user = menu()
 		elif user == 4:
 			print "Good-bye!\n"
 			return False

if __name__ == '__main__':
 	main()

	



