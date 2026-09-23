# Program Name: IT3883 Assignment1.py
# Course: IT3883 W01
# Student Name: Miles Johnson
# Assignment Number: Assignment 1
# Due Date: 09/22/2026
# Purpose: This program provides a text based menu that allows the user to
#          append text to an input buffer, clear the buffer, display the
#          current buffer contents, or exit the program.


# Create an empty string that will store all text entered by the user.
input_buffer = ""

# Keep displaying menu until user chooses exit option.
while True:
    print("\n--- Input Buffer Menu ---")
    print("1. Add data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    # Ask user to select one of four menu options.
    choice = input("Enter your choice (1-4): ")

    # Option 1: Add new text to the end of existing buffer.
    if choice == "1":
        new_data = input("Enter a string to append: ")
        input_buffer += new_data
        print("Data added to input buffer.")

    # Option 2: Remove all text currently stored in buffer.
    elif choice == "2":
        input_buffer = ""
        print("Input buffer has been cleared.")

    # Option 3: Display text currently stored in buffer.
    elif choice == "3":
        if input_buffer:
            print("Current input buffer:", input_buffer)
        else:
            print("Input buffer is currently empty.")

    # Option 4: End program.
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    # Handle any menu choice that is not 1, 2, 3, or 4.
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
