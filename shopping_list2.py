
import os
def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')	

# to make a list of entered items
shopping_list = []

empty_line = """

"""

def show_help():
	# print out instructions on how to use the app
	print("What should we buy at Auchan?")
	print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")

def show_list():
	# print the list out
	print("Here is our list:")

	for item in shopping_list:
		print(item)

def add_to_list(new_item):
		# add new items to our list
	shopping_list.append(new_item)
	print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

show_help()

while True:
	# ask for new items
	new_item = input("> ")

	# be able to quit the app
	if new_item == 'DONE':
		break
	elif new_item == 'HELP':
		show_help()
		continue
	elif new_item == 'SHOW':
		show_list()	
		continue
	add_to_list(new_item)


show_list()
with open(os.path.join(os.path.expanduser('~'),'Documents', "Shopping list.txt"), "w", encoding='utf-8') as text_file:
    for item in shopping_list:
        text_file.write(item + "; " + empty_line)

clear()  