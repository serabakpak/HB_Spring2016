# This is a comment and it not read by the interpreter
# These are useful for describing difficult code or adding reminders.
# TODO - fix this code :D
# (Part 1): Instead of using the hard coded ".18",
# Ask the user to input the percentage of tip they want to give. 
# Save the input to a variable. 
# Use the variable to calculate the tip.
# (Part 2): Fix any bugs and make it work!

bill = float(raw_input("How much was your bill? "))
tip = float(raw_input("Enter the percentage of tip you want to leave: "))

total_bill = bill + bill*(tip/100)

print "The tip is %f and the total bill is %f ." % (float(tip), float(total_bill))