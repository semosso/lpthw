# CREATES function; ln 2 says which values it needs (could be any name), others say what function does
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f'You have {cheese_count} cheeses!')
    print(f'You have {boxes_of_crackers} boxes of crackers!')
    print('Man, that\'s enough for a party!')
    print('Get a blanket.\n')


print('We can just give the function numbers directly:')
# calls function, assigning its values by giving straight numbers
cheese_and_crackers(20, 30)
# note that assigning 20 and 30 in ln 11 only work for THIS SPECIFIC run of the function, they don't change its values permanently
## remember then to assign different names to the values a function needs (its variables) and those global to the script

print('OR, we can use variables from our script:')
amount_of_cheese = 10
amount_of_crackers = 50
# calls function, assigning its values with variables, defined above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print('We can even do math inside too:')
# calls function, assigning its values with math
cheese_and_crackers(10 + 20, 5 + 6)


print('And we can combine the two, variables and math:')
# calls function, assigning its values by combining math and variables
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)