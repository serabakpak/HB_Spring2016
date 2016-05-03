
"""SHOULD YOU EAT THAT BACON? - this is a program that determines whether or not you should eat bacon."""


def ask_if_angels():
	user_angels = None
	try:
		user_angels = int(raw_input('\nDo you want to feel like angels are frolicking on your taste buds?\nType 1 for YES\nType 2 for NO\nType 3 for YES, BUT I AM AFRAID IT WILL KILL ME!\n'))
	except BaseException:
		print("\nDo you know how to follow instructions? IDIOT!")
		ask_if_angels()

	if user_angels == 1:
		print("EAT IT!\n")
	elif user_angels == 2:
		print("You've clearly never tasted bacon. EAT IT!\n")
	elif user_angels == 3:
		ask_if_coward()
	else:
		print("\nDo you know how to follow instructions? IDIOT!\n")
		ask_if_angels()
	
def ask_if_coward():
	
	user_coward = str.upper(raw_input("Are you a coward? YES or NO?" ))
	if user_coward == "YES":
		print("Bacon will turn you into a true warrior!")
	else:
		print("THEN EAT IT!")

def main():
	
	while True:
		user_intro = str.upper(raw_input('\nWelcome to "Should You Eat That Bacon?" Would you like to continue? Type YES or NO! '))
		
		if user_intro == "YES":
			ask_if_angels()
			return
		
		elif user_intro == "NO":
			return


if __name__ == '__main__':
	main()



