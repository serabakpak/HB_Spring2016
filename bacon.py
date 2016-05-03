
"""SHOULD YOU EAT THAT BACON? - this is a program that determines whether or not you should eat baconself."""


def ask_if_angels():
	user_angels = int(raw_input('Do you want to feel like angels are frolicking on your taste buds?\nType 1 for YES\nType 2 for NO\nType 3 for YES, BUT I AM AFRAID IT WILL KILL ME! '))
	if user_angels == 1:
		print("EAT IT!")
	elif user_angels == 2:
		print("You've clearly never tasted bacon. EAT IT!")
	elif user_angels == 3:
		ask_if_coward()


def ask_if_coward():
	user_coward = str.upper(raw_input("Are you a coward? YES or NO?" ))
	if user_coward == "YES":
		print("Bacon will turn you into a true warrior!")
	else:
		print("THEN EAT IT!")

def main():
	print''
	
	user_intro = str.upper(raw_input('Welcome to "Should You Eat That Bacon?" Would you like to continue? Type YES or NO! '))
	
	if user_intro == "YES":
		ask_if_angels()
	
	elif user_intro == "NO":
		return

if __name__ == '__main__':
	main()



