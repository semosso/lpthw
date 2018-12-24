# i = 0
# numbers = []

# while i < 6:
#     print(f'At the top i is {i}')
#     numbers.append(i)

#     i = i + 1
#     print('Numbers now: ', numbers)
#     print(f'At the bottom i is {i}') # goes to top until i < 6, that's the whole point of the WHILE-loop


# print('The numbers: ') # only called when loop ends, i.e., when i = 6, and lists is 0 through 5

# for num in numbers:
#     print(num) # prints each number, one at a time, until reaches the last NUM (it'd be different if it was NUMBERS, because it'd print the list six times)

# # # # STUDY DRILLS
# # # 1, convert this while-loop to a FUNCTION that you can call, and replace 6 in the test with a variable
# # # 2, use this FUNCTION to rewrite the script to try different numbers

# def lister(fim):
#     i = 0
#     lista = []
    
#     while i < fim:
#         print(f'At the top i is {i}')
#         lista.append(i)

#         i = i + 1
#         print('Numbers now: ', lista)
#         print(f'At the bottom i is {i}')
#     return lista # important indent here (I got it right the first time by luck; this should be indented to the function level, not the while-loop)

# var = int(input('How long should the loop run for?\n> ')) # important, so that comparison in ln 24 works (otherwise input comes as string)

# lishta = lister(var)

# print('The numbers: ')

# for num in lishta:
#     print(num)

# # 3, add another variable to the FUNCTION arguments that you can pass in that lets you change the + 1 on line 8 so you can change how much it increments by
# # 4, rewrite the script again to use this function to see what effect that has

# def lister2(fim, incremento):
#     i = 0
#     lista = []

#     while i < fim:
#         print(f'At the top i is {i}')
#         lista.append(i)

#         i = i + incremento
#         print('Numbers now: ', lista)
#         print(f'At the bottom i is {i}')
#     return lista

# var2 = int(input('How long should the loop run for?\n> '))
# incr = int(input('What should the increment be?\n> '))

# lishta2 = lister2(var2, incr)

# print('The numbers: ')

# for num in lishta2:
#     print(num)

# 5, write it to use for-loops and range. Do you need the incrementor in the middle anymore? What happens if you do not get rid of it?

i = 0
numbers = []

for i in range (0, 6): # no need for incrementor, because FOR-LOOP "iterates over" each element within range in a sequence
    # note how 6 being the last number in RANGE is similar to having WHILE i < 6, because range doesn't iterate over last number
    print(f'At the top i is {i}')
    numbers.append(i)

    i = i + 1
    # no need for it; if we do use it, however, ln 82 returns 6 instead of 5; why is that?
    # note that "i" in for-loop is not the i=0 variable (it could be X, Y, Z, whatever, it would still work); but i at ln 80 IS THE SAME as i=0, so every
    # time that the for-loop runs, it gets incremented by 1; STOPPING EVERYTHING, WHY DID I GET A FEW "AT THE BOTTOM I IS 0" ABOVE? should that have happened?
    print('Numbers now: ', numbers)
    print(f'At the bottom i is {i}')

print('The numbers: ')

for num in numbers:
    print(num)