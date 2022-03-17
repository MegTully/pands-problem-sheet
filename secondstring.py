#This program allows you to enter a sentence 
# and returns a string with every second letter starting from the end 
#of the sentence.
#Author: Megan Tully

#Asks user to write a sentence
sentence = str(input("Enter a sentence: "))

#Creates a new string starting with last letter of sentence(sentence backwards) [1]
Backwards= sentence[::-1]

#prints out every second letter of sentence backwards [1]
print(Backwards[0::2]) 

#[1] Strings and Character Data in Python, Christopher Bailey, https://realpython.com/lessons/string-slicing/
