#=========================================================CALCULATOR APP================================================================#

#=========================================================FUNCTIONS================================================================#

# Define each function for the calculator using mathematical operators, with num_1 and num_2 as parameters

def add(num_1,num_2):
    return num_1 + num_2

def subtract(num_1,num_2):
    return num_1 - num_2

def multiply(num_1,num_2):
    return num_1 * num_2

def divide(num_1,num_2):
    return num_1 / num_2

# Define functions for writing and opening the file

def write_file(value):

# Use exception handling if the file does not exist
# Prompt user to write a file name using input
# Write user data 
# Close file

    text_file = None
    try:
            text_file_write = input("\n\nPlease enter the file name that you would like to save these calculations on, followed immediately by .txt:\n\n").lower()
            text_file = open(text_file_write, "a+", encoding = "utf-8")

            text_file.write(value)

            text_file.close()

    except FileNotFoundError as error:
        print("This file does not exist")
        print(error)

    finally:
        if text_file is not None:
            text_file.close()

    print(f"\n\nThank you, your calculation has been added to {text_file_write}.\n")

def open_file():

# Use exception handling if the file does not exist
# Prompt user to choose file name to open
# Print data
# Close file

    text_file = None

    try:
            text_file_name = input("\n\nPlease enter the name of the file you would like to open, followed by .txt:\n\n").lower()

            text_file = open(text_file_name, "r", encoding = "utf-8")

            print("\n--------------------------CALCULATIONS--------------------------\n")

            for lines in text_file:
                print(f'''
                {lines}''')

            print("\n--------------------------END----------------------------------\n")

            text_file.close()

    except FileNotFoundError as error:
        print("\nThis file does not exist")
        print(error)
        
    finally:
        if text_file is not None:
            text_file.close()

#=========================================================MENU=====================================================================#

# Use a loop to go through menu choices

while True:
    try:
        input_choice = int(input('''\nPlease select from the following:\n
                                1. Add\n
                                2. Subtract\n
                                3. Multiply\n
                                4. Divide\n
                                5. View all calculations\n
                                6. Quit\n'''))

# If user selects 1, add num_1 and num_2
# Print results and call write_file() function

        if input_choice == 1:
            user_num_1 = int(input("\nPlease enter your first number:\n\n"))
            user_num_2 = int(input("\nPlease enter your second number:\n\n"))

            answer = (f"The sum of {user_num_1} and {user_num_2} is {add(user_num_1,user_num_2)}\n")

            print("\n",answer)
            write_file(answer)

# If user selects 2, subtract num_1 and num_2
# Print results and call write_file() function

        elif input_choice == 2:
            user_num_1 = int(input("\nPlease enter your first number:\n\n"))
            user_num_2 = int(input("\nPlease enter your second number:\n\n"))

            answer = (f"The subtraction of {user_num_1} and {user_num_2} is {subtract(user_num_1,user_num_2)}\n")

            print("\n",answer)
            write_file(answer)

# If user selects 3, subtract num_1 and num_2
# Print results and call write_file() function

        elif input_choice == 3:
            user_num_1 = int(input("\nPlease enter your first number:\n\n"))
            user_num_2 = int(input("\nPlease enter your second number:\n\n"))


            answer = (f"The multiplication of {user_num_1} and {user_num_2} is {multiply(user_num_1,user_num_2)}\n")

            print("\n",answer)
            write_file(answer)

# If user selects 4, divide num_1 and num_2
# Use a try except if the user tries to divide by 0
# Print results and call write_file() function

        elif input_choice == 4:
            while True:
                try:
                    user_num_1 = int(input("\nPlease enter your first number:\n\n"))
                    user_num_2 = int(input("\nPlease enter your second number:\n\n"))

                    answer = (f"The division of {user_num_1} and {user_num_2} is {divide(user_num_1,user_num_2)}\n")
                    print("\n",answer)
                    write_file(answer)
                    break
                except:
                    ValueError(print("\nDivision by 0 is not defined. Please select a number greater than 0."))

# If user selects 5, call open_file() function

        elif input_choice == 5:
            open_file()

# If user selects 6, break the loop 

        elif input_choice == 6:
            print("\nHave a lovely day!\n")
            break

# If the user selects a number out of range, prompt accordingly

        elif input_choice > 6:
            print("\nYou have selected an invalid option. Please try again by choosing from the menu below.\n")

# Use a try except ValueError if the user inputs letters instead of numbers

    except ValueError:
        print("\nYou have selected an invalid option. Please try again by entering a number.\n")

#=========================================================END OF CODE=============================================================#
    

