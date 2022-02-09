#This program allows you to enter a sentence 
# and returns a string with every second letter starting from the end 
#of the sentence.
#Author: Megan Tully

sentence = str(input("Enter a sentence: "))
print(sentence[::-1])