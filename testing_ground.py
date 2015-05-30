__author__ = 'Wade'

# my_int is set to 7 below. What do you think
# will happen if we reset it to 3 and print the result?

my_int = 7

# Change the value of my_int to 3 on line 8!

my_int = 3

# Here's some code that will print my_int to the console:
# The print keyword will be covered in detail soon!

print my_int
print type(my_int)


def spam():
    """

    :rtype : object
    :return:
    """
    eggs = 12
    return eggs


print spam()

# this is a comment
monty = True
python = 1.234
monty_python = python ** 2

print "monty = "
print monty
print python
print monty_python

# region Stringfall section: use the escape character
# The string below is broken. Fix it using the escape backslash!
# endregion

stringfall = 'This isn\'t flying, this is falling with style!'
print stringfall


# Insert a variable!
# This method uses a "conversion specifier"

testStringInsertion = "monty = %s" % monty
print testStringInsertion

string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)


# Four string methods:
#
#     1. len()
#     2. lower()
#     3. upper()
#     4. str()
#
# Methods that use dot notation only work with strings.
# On the other hand, len() and str() can work on other data types.
#



parrot = "Norwegian Blue"
print len(parrot)

parrotLowered = parrot.lower()
print parrotLowered
print "Another Norwegian Blue".lower()

print parrot.upper()

pi = 3.14
print str(pi)

# concatenate with the + sign:
print "Spam" + " and " + "eggs"


# import from datetime to use it
# pull whatever date, time, year, hour, minute, second you want

from datetime import datetime
now = datetime.now()

current_year = now.year

print '%s-%s-%s' % (now.year, now.month, now.day)

print '%s/%s/%s' % (now.month, now.day, now.year)

print '%s:%s:%s' % (now.hour, now.minute, now.second)


# defining a program, comparing inputs, and using if-then

def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()


# conditionals: and, or, not, xor

bool_one = False and False   #false
if bool_one == True:
    print "Yes!"
elif bool_one == False:
    print "Nope."
else: 
    print invalid
    
bool_four = -(1**2) < 2**0 and 10 % 10 <= 20 - 10 * 2   #true
if bool_four == True:
    print "Yes!"
elif bool_four == False:
    print "Nope."
else: 
    print invalid    
