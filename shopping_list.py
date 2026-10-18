shopping_list = []

print("Welcome to your Shopping List Manager!")

while True:
    action = input("\nChoose an action (add / remove / show / done): ").strip().lower()
    
    if action == "add":
        item = input("Enter the item to add: ").strip()
        shopping_list.append(item)
        print(f"'{item}' has been added.")
        
    elif action == "remove":
        item = input("Enter the item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed.")
        else:
            print("That item is not on your list.")
            
    elif action == "show":
        print("\nYour Current Shopping List:")
        if not shopping_list:
            print("  (Your list is empty)")
        else:
            for item in shopping_list:
                print(f"- {item}")
                
    elif action == "done":
        print("\nThank you for using the Shopping List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please type add, remove, show, or done.")
