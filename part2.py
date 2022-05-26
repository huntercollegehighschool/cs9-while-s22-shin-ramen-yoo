'''
***PART 2***

Write a program that prompts the user to enter a number. The program then prints "Hunter" the number of times the user entered. Use a while loop.

Example of what should appear when the program runs:

Times to print: 3
Hunter
Hunter
Hunter

'''
timesprinted = int(input("Enter a number: "))
counter = 0

while counter < timesprinted:
  counter = counter + 1
  print("Hunter") 