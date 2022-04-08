#This program outputs whether or not today is a weekday.
#Author : Megan Tully

#need to import datetime package
import datetime

# returns the day of the week as an integer where monday is 1 and sunday is 7 and assigns it a variable name Today 
Today = datetime.datetime.today().isoweekday()#[1],[2]

#Create an if statement that prints it is a weekday if Today is less than 6 
if Today < 6:
    print("Yes, unfortuneately today is a Weekday")

#Otherwise print its the weekend
else:
    print ("It is the weekend, yay!")

#Print whether its a weekday or weekend
print(Today) 


#[1] python.org, basic date and time types, https://docs.python.org/3/library/datetime.html#datetime.date.isoweekday
#[2] StackOverflow, https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date