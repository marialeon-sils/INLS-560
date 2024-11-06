# Prime the while loop
menu_option = ''

# Create the while loop; any key keeps it running, only 'q' quits
while menu_option != 'q':
    # Display the menu using an f-string
    print(f"""
Shop Information FAQS:
a - Tips for dog care
b - Tips for cat care
c - Tips for other animals
q - Quit
Please enter a letter:
    """)

    # Get user input
    menu_option = input("> ")

    # Handle menu options with if-elif statements and a nested prompt
    if menu_option == 'a':
        print("Dog Care Tip: Make sure your dog gets proper exercise and daily walks.")
        additional_info = input("Would you like more information? (y/n): ")
        if additional_info.lower() == 'y':
            print("Tip: Be patient with your dog and use positive reinforcement!")
        else:
            print("Back to main menu.")

    elif menu_option == 'b':
        print("Cat Care Tip: Make sure your cat is hydrated.")
        additional_info = input("Would you like more tips on cat hydration? (y/n): ")
        if additional_info.lower() == 'y':
            print("Tip: Elevated bowls encourage cats to drink more!")
        else:
            print("Back to main menu.")

    elif menu_option == 'c':
        print("Other Animal Care Tip: Make sure your pet has a proper diet.")
        additional_info = input("Would you like more tips on diets? (y/n): ")
        if additional_info.lower() == 'y':
            print("Tip: Research the appropirate diet for your pet!")
        else:
            print("Back to main menu.")

    elif menu_option == 'q':
        print("Thank you for using Pet Tips!")
    
    else:
        print("Invalid input! Please enter 'a', 'b', 'c', or 'q'.")
