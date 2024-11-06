# Prime the while loop
menu_option = ''

# Create the while loop; any key keeps it running, only 'q' quits
while menu_option != 'q':
    # Display the menu with `sep='\n`
    print("PET TIPS MENU:",
          "a - Tips for dog care",
          "b - Tips for cat care",
          "c - Tips for other animals",
          "q - Quit",
          "Please enter a letter:",
          sep="\n")

    # Get user input
    menu_option = input("> ")

    # Handle menu options with if-elif statements
    if menu_option == 'a':
        print("Dog Care Tip: Make sure your dog gets proper exercise and daily walks.")
    
    elif menu_option == 'b':
        print("Cat Care Tip: Make sure your cat is hydrated.")
    
    elif menu_option == 'c':
        print("Other Animal Care Tip: Make sure your pet has a proper diet.")

    elif menu_option == 'q':
        print("Thank you for using Pet Tips!")
    
    else:
        print("Invalid input! Please enter 'a', 'b', 'c', or 'q'.")
