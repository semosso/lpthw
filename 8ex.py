# creates the 'formatter' variable, assigns it a STRING with four additional variables embedded in it
formatter = '{} {} {} {}'

# FORMAT is a function that calls the variable FORMATTER and gives it ARGUMENTS
# calling the variable's FORMAT function (i.e., telling it to do a command line command named format)
# the result of calling FORMAT on the formatter variable is a new string with the arguments that FORMAT gives it
print(formatter.format(1, 2, 3, 4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, False, True)) # no quotes needed because python recognizes this as keywords for T/F; same as ln 7
print(formatter.format(formatter, formatter, formatter, formatter)) # you can loop the variable inside itself
print(formatter.format(
    'Try your', # why didn't it include a \n at the end here? is it only at right before the closing ), i.e., line 14?
    'Own text here',
    'Maybe a poem',
    'Or a song about fear'
)) # note the indent; this will become important later on, if you move indent around you fuck up your code

# DRILLS
# what if I give a different number or ARGUMENTS than the original VARIABLE has?
formatter = '{} {} {} {}'
print(formatter.format(1, 2, 3)) # lower number of arguments results in an error
print(formatter.format(1, 2, 3, 4, 5)) # higher number of arguments does not result in an error, just leaves the extra ones out of it