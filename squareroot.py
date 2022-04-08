#This program takes a positive floating-point number as input and outputs an approximation of its square root
#using Newton-Raphson method for square roots: root = 0.5 * (N + (X / N)) where N is any guess which can be 
#assumed to be X or 1. [1]

#function defines how to get the average of 2 numbers a and b
def average(a, b):
    #average of 2 numbers = 2 numbers added divided by 2
    return (a + b) / 2.0

#function takes parameter guess and user input x and returns the average of guess and x/guess [4]
def improve(guess, x):
    #Newton-Raphson method [1]
    return average(guess, x/guess)

#function checks if the difference d between the guess squared and the user input x is less than 0.001
def good_enough(guess, x):
    #calculates absolute value of guess^2 minus the desired root^2 [2],[3]
    d = abs(guess*guess - x)
    return (d < 0.001)

#function takes in 2 parameters guess and x
def square_root(guess, x):
    #while loop says while the function good_enough is not true for d< 0.001 [4],[5]
    while(not good_enough(guess, x)):
        #call function improve() and assign new value to guess
        guess = improve(guess, x)
    #returns new value
    return guess

#function calls on square_root function with parameters guess =1 and x = user input [1]
def sqrt(x):
    r = square_root(1, x)
    #returns the square root of x
    return r

x = float(input("Please Enter a positive number: "))
#prints out the result rounded to one decimal place [6]
print("The square root of",x, "is approx.", round(sqrt(x),1))


#[1] https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.   
#[2] https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
#[3] https://stackoverflow.com/questions/20811208/newton-s-method-for-finding-square-roots-in-python
#[4] https://math.stackexchange.com/questions/3524205/square-roots-by-newton-s-method
#[5] https://python.pages.doc.ic.ac.uk/2021/lessons/lesson04/05-break/06-newtonsolution.html
#[6] https://www.knowledgehut.com/blog/programming/python-rounding-numbers