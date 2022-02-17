# Programmer: Susie LaMonica
# Course: CS 151.02, Dr. Olsen
# Homework Assignment: 4
# Purpose: The purpose of this code is to take the user through a set of choice points, so that I can then draw a
# flowchart based off the decision points, to get practice with making more complicated flowcharts.

# Greet the user
print ("Hi! Time to make some choices!")

# choice 1
favorite_color = input("Please input your favorite color: ")

if favorite_color == "pink":
    print ("That's my favorite color!")
elif favorite_color == "yellow":
    print ("Yellow reminds me of summertime.")
else:
    print ("Nice!")

# choice 2
favorite_dessert = input("What is your favorite dessert?: ")

if favorite_dessert == "cookies":
    print ("Yum! Chocolate chip are my favorite kind of cookie")
elif favorite_dessert == "brownies":
    print ("Delicious")
else:
    print ("Yummy!")

print ("Thanks for making some choices!")