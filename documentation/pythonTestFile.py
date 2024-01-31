
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                     PROGRAM INFORMATION
#                                                   Programmer : Blaise Como
# Date       : Tuesday July 27th, 2021
# Filename   : average_of_nums.py
# Purpose    : This program caclulates the average of a list of numbers on a file, it then writes the values and average into an ouput file named by the user
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
# When this program is run, you will see the average of the numbers as well as the numbers themselves in the terminal, and a seperate file that the user names will be created with this information
# Importing turtle to use a dialog box
import turtle

## Displays the average of the list of numbers as well as the numbers themselves in an organized list
#  @param none
#  @return Content of the output file
def avg_of_nums():

    # Opens the numbers.txt to be read
    num_file = open('numbers.txt', 'r')

    # Assigns the user picked file name to a variable
    user_name = turtle.textinput("Output file name", "")

    # Empty list to append numbers from numbers.txt to
    nums1 = []

    # Loop to iterate through numbers.txt and append them to nums1 as integers
    for num in num_file:

        nums1.append(int(num))

    # Closing of the numbers.txt object
    num_file.close()
    
    # Variable for the average of the numbers from the file
    avg = sum(nums1) / len(nums1)

    # Opening and creation of the output file using the write mode
    output_file = open(user_name, 'w')

    # Writes the average of the numbers to the file
    output_file.write("Average of given numbers: {}".format(str(avg)))
    
    # Writes the numbers to the file after the average
    output_file.write(", Numbers: {}".format(str(nums1)))

    # Closing of file so it can be opened in read mode
    output_file.close()

    # Opening of the output file in read mode
    output_file = open(user_name, 'r')

    # Returns the contents of the output file so that it can be seen by the user
    return output_file.read()

    # Closing of the output file
    output_file.close()

# Try statement for the calling and printing of the function
try:
    print(avg_of_nums())
# Exception handler for if the file is named wrong
except FileNotFoundError:
    print("File is unable to be found")
# Another exception handler for if there are other issues with the code
except: 
    print("Oops! Something is wrong with the code.")








