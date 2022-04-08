# Task06: Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. Create a function called sqrt that does this. 
## Author: Megan Tully

## Function One: sqrt(), finding square root of a number using Newton-Raphson method
The Newton-Raphson method was used to calculate the square root which is defined as root = 0.5 * (N + (X / N)) where N is any guess which can be assumed to be X or 1 on the website geeksforgeeks[1]. To write this program a recursive method was used so it starts with the sqrt function at the end and works backwards. This method reiterates until the best possible root is found. The sqrt() function takes in 1 parameter x which is the integer the user inputs to the program, i.e the number they want the square root of. It then passes the values 1 and x into the previous function called square_root() as it's parameters. 

## Function Two: square_root() 
The square_root function then takes in the value 1 as its parameter "guess" and x as the value the user input. Within this function the while loop says that while the previous function called good_enough is not true, i.e the difference in closeness between the guess squared and x is too large (>0.001), call on the function improve(). The new value returned from the function improve() is assigned as the new guess value. This loop will keep running until good_enough returns true.

## Function Three: good_enough()
The good_enough function returns a value of true or false. It calculates the precision [2] by checking if the difference between the guess squared and x is smaller than 0.001. This is calculated by getting the absolute value of guess squared minus x which is assigned the variable name "d". If d < 0.001 then the function returns true if not it returns false. For every new value assigned to the variable "guess" this function run until it returns true.

## Function Four: improve()
The improve function is called upon by the square_root function to improve the guess. This is the function that carries out the formula for Newton-Raphsons method. It does this by getting the average of the guess and x divided by the guess and returns the result[1]. To get the average this function calls on the previous function created called average.

## Function Five: average()
The average function takes in two parameters a and b and returns their average. It does this by adding the two numbers together and divides them by two. Then returns the result.

## Result:
Starting off with a guess of 1 and an integer input by the user called x, this recursive program reiterates for different values of the variable "guess" and on each iteration the values of guess squared get closer and closer to x until they get as close as posible then we can say "guess" is an appropriate approximation of the square root of x. The program then prints out the square root of the number x rounded to one decimal place.








#[1] https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.   
#[2] https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
#[3] https://stackoverflow.com/questions/20811208/newton-s-method-for-finding-square-roots-in-python
#[4] https://math.stackexchange.com/questions/3524205/square-roots-by-newton-s-method
#[5] https://python.pages.doc.ic.ac.uk/2021/lessons/lesson04/05-break/06-newtonsolution.html