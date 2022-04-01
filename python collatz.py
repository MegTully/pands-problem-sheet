#This program allows the user to input an integer,then calculates the next value by taking the current value
#and, if it is even, divides it by two, but if it is odd, multiplies it by three and adds one.
#The program ends if the current value is one.
#Author: Megan Tully

#Ask the user to input a number, int() ensures its an integer, variable name is number 
number = int(input("Enter a positive integer: "))

#Create a while loop to make the program is only ran while number is greater than or equal to 1,i.e positive
while number >= 1:
    #print the number after each iteration of the loop
    print(number, end=" ") #[2] putting (end= " ") in the print statement puts the output of each iteration on the same line separated by a space
    #Divide the number by two if it is even and assign the new value to variable number
    if (number % 2 == 0):
        number=number//2

    #If the number is equal to one, terminate the loop
    elif number == 1:
        break           #[1] break statement terminates the loop

    #Otherwise if the number is not even or equal to 1, multiply it by 3 and add 1, assign the new value to variable number
    else:
        number=(number*3) +1


#[1]TutorialsPoint,https://www.tutorialspoint.com/python/python_loop_control.htm#:~:text=The%20break%20statement%20in%20Python,both%20while%20and%20for%20loops.
#[2]StackOverflow, https://stackoverflow.com/questions/12032214/print-new-output-on-same-line