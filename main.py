print("The List Manager")

def my_fuc():
	import sys
	import os
	import time

	print("Choose from the following options")
	print("")

	todo_list = []

	while True:
		time.sleep(3)
		os.system('cls' if os.name == 'nt' else 'clear')

		print("1. View Items")
		print("2. Add Item")
		print("3. Remove Item")
		print("4. Edit Item")
		print("5. Clear List")
		option = input("Enter your option: ")

		#view Items
		if option == "1":
			if not todo_list:
				print("No items to view")
			else:
				for i, item in enumerate(todo_list):
					print(f"{i+1}. {item}")

		#add Item

		elif option == "2":
			item = input("Enter the item to add: ")
			if item in todo_list:
				print("Item already exists")
			else:
				todo_list.append(item)
				print("Item added")

		#remove Item
		elif option == "3":
			item = input("Enter the item to remove: ")
			if not item in todo_list:
				print("Item does not exist")
			else:
				confirmation = input("Are you sure you want to remove this item? (y/n) ")
				if confirmation == "y":
					todo_list.remove(item)
					print("Item removed")

			#edit Item
				elif option == "4":
					item = input("Enter the item to edit: ")
					if not item in todo_list:
						print("Item does not exist")
					else:
						confirmation = input("Are you sure you want to edit this item? (y/n) ")
						if confirmation == "y":
							new_item = input("Enter the new item: ")
							if new_item in todo_list:
								print("Item already exists")
							else:
								todo_list[todo_list.index(item)] = new_item
								print("Item edited")

				#clear List
						elif option == "5":
							todo_list = []
							print("List cleared")

		else:
			print("Invalid option")


my_fuc()
