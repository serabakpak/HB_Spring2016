# Prompt
# We are going to continue to modify our bart_kiosk_simulator.py file.  We will have a List that contains all of the stops on the Dublin/Pleasanton Bart line.  

# start_point is an Integer that corresponds to the List index of the station where you want to board the train
# end_point is an Integer that corresponds to the List index of the destination station.
# start_point and end_point should be used to slice a sublist from the bart_line List.
# Assuming that a stop at each station costs $1.25, print out the names of all the stops between your origin station and destination station, as well as how much it would cost to travel between the two stations.
# Return the calculated cost from the function and save it into a variable named fare_price

def calculate_fare(bart_line, start_point, end_point):
	if start_point < end_point:
		trip = bart_line[start_point:(end_point + 1)]
	elif start_point > end_point:
		trip = bart_line[start_point:(end_point - 1):-1]
	print trip
	fare_price = abs(len(trip) - 1) * 1.25
	return fare_price
	
#bart_line_stations_list is a list that holds the names of stations found on a single BART line.

def choose_destination(bart_line_stations_list):
	station_indexes = []
	print bart_line_stations_list
	starting_station_name = raw_input("Where are you boarding the train? ")
	#starting_station_name = starting_station_name.capitalize()
	
	if starting_station_name in bart_line_stations_list:
		starting_station_index = bart_line_stations_list.index(starting_station_name)
		station_indexes.append(starting_station_index)
	else:
		print "The BART station you entered does not exist."
 	destination_station_name = raw_input("What is your destination? ")
 	#destination_station_name = destination_station_name.capitalize()
 	if destination_station_name in bart_line_stations_list:
		destination_station_index = bart_line_stations_list.index(destination_station_name)
		station_indexes.append(destination_station_index)
	else:
		print "The BART station you entered does not exist." 
	return station_indexes

def main():
	DUBLIN_PLEASANTON = ["Dublin/Pleasanton", "West Dublin/Pleasanton", "Castro Valley", "Bay Fair", "San Leandro", "Coliseum", "Fruitvale", "Lake Merritt", "West Oakland", "Embarcadero", "Montgomery St.", "Powell St.", "Civic Center/UN Plaza", "16th St. Mission", "24th St. Mission", "Glen Park", "Balboa Park","Daly City"]
	station_numbers = choose_destination(DUBLIN_PLEASANTON)
	fare = calculate_fare(DUBLIN_PLEASANTON, station_numbers[0], station_numbers[1])
	
	print "Your trip costs $" + str(fare)

if __name__ == '__main__':
	main()


# Tests
# Call calculate_fare with DUBLIN_PLEASANTON, 0, 4 as inputs and print the output. This should print ['Dublin/Pleasanton', 'West Dublin/Pleasanton', 'Castro Valley', 'Bay Fair', 'San Leandro'],  6.25.
# Call calculate_fare with DUBLIN_PLEASANTON, 7, 15 as inputs and print the output. This should print 
# ['Lake Merritt', 'West Oakland', 'Embarcadero', 'Montgomery St.', 'Powell St.', 'Civic Center/UN Plaza', '16th St. Mission', '24th St. Mission', 'Glen Park', 'Balboa Park']
#12.5.


# Bonus
# Currently, our function is only written to account for traveling in one direction, westbound toward Daly City.  What if we wanted to travel eastbound towards Dublin/Pleasanton.  We should account for traversing the list in reverse.  Modify your calculate_fare function to account for traversing in either direction.  Hint: you can use a negative step to traverse a list in reverse.  Example: DUBLIN_PLEASANTON[6:3:-1] slices from index 6 to index 3 in reverse order.

