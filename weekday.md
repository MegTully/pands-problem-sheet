# Task05: Write a program that outputs whether or not today is a weekday. 
## Author: Megan Tully

## Step One: Import package
In order to write this program we need to use the datetime function so we first need to import the datetime package

## Step Two: Determine what day of the week it is
After reasearching the internet I found a method on the website StackOverflow that can be used to determine whether the current day is a weekday or weekend. The method, datetime.datetime.today(), returns the current local date. Then I clicked a link also in this StackOverflow[2] answer which brought me to a website called python.org[1] where I took the method .isoweekday which returns the day of the week as an interger where 1 is Monday and 7 is Sunday. Therefor 1-5 are weekdays and 6-7 are the weekend. These methods were put together and assigned the variable name Today.

## Step Three: Create an if statement
An if statement was created to print "Yes, unfortuneately today is a Weekday" if the current day is a weekday. This is determined by using the fact that the variable Today will be between 1 and 5, i.e Today<6, if it is a weekday. The else statement says otherwise print "It is the weekend, yay!" which would be when Today is > 5.

## Step Four: Return the result
A print() statement was used to return the variable Today which tells the user if it is a weekday or weekend.
