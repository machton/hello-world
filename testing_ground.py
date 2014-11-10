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


