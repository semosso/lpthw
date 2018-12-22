people = 30
cars = 40
trucks = 15


if cars > people: # if boolean expression is True, print; if False, check if elif is True, print; if False, go to else and print
    print('We should take the cars.')
elif cars < people: # this is just like a second check to see whether you get a True return on some other expression, before resorting on the False
# python only checks for the first True, then it prints (e.g., if both if and elif were true (e.g., > and "not <"), it'd only print the first sentence)
# note that, because of that, you need to add a boolean expression (i.e., a test) to elif, it's not like else (which just feeds of IF being False)
    print('We should not take the cars.')
else: # this would only happen because we're not using "or equal" in lines above (i.e., >= or <=)
    print('We can\'t decide.')

if trucks > cars: # if boolean expression is True, print; if False, check if elif is True, print; if False, go to else and print
    print('That\'s too many trucks.')
elif trucks < cars: # this is just like a second check to see whether you get a True return on some other expression, before resorting on the False
    print('Maybe we could take the trucks.')
else: # this would only happen because we're not using "or equal" in lines above (i.e., >= or <=)
    print('We still can\'t decide.')

if people > trucks: # if boolean expression is True, print; if False, print ln 23
    print('Alright, let\'s just take the trucks.')
else:
    print('Fine, let\'s stay home then.')