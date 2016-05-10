# Write a Todo List program
# Create functions to maintain the Todo list:
# add_element() that takes a list and a string and returns the modified array
# delete_element() that takes a list and an index and returns the modified array
# list_element() that takes an array and presents it neatly

todo_list = ['clean room', 'cook', 'eat']

def add_element(list, item):
	list.append(item)
	return list

def delete_element(list, i):
	list.pop(i)
	return list

def list_element(list):
	list.sort()
	for item in list:
		print "[ ] " + item
	

def main():
	print add_element(todo_list, 'buy clothes')
	print delete_element(todo_list, 1)
	list_element(todo_list)

if __name__ == '__main__':
	main()





