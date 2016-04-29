if 8 % 2 == 0 and 9 % 2 == 0:
	print "Both numbers are even."
elif 8 % 2 == 0 and 9 % 2 == 1:
	print "8 is even and 9 is odd."
elif 9 % 2 == 0 and 8 % 2 == 1:
	print "9 is even and 8 is odd."	
else:
	print "Both numbers are odd."



fav_color = "blue"
if fav_color == "blue":
	print "My fav color is blue!"
else:
	print "My fav color is not blue."

fav_color = "yellow"
if fav_color == "blue" or "yellow" or "red":
	print "My fav color is a primary color."
else:
	print "My fav color is a secondary color."


input = raw_input("Did you finish Activity 1?")
done = None

if (str.lower(input) == "yes"): #why do this?
    done = True
else: 
	done = False

if not done:
    print "Please continue with Activity 1."
else: 
	print "Please move on to Activity 2."