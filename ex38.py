ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(" ") # ten_things wasn't a LIST, but a STRING; by splitting it based on the empty space separators, you create a list with the separated items
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1]) # it should be Oranges
print(stuff[-1]) # last one, so "Frisbee"? depends on how pop() and append () will work -- NOPE, pop works from right to left, so CORN
print(stuff.pop()) # Apples? depends on whether pop with no arguments pops the top one (i.e., position 0) -- NOPE, pop works from right to left, so CORN
print(" ".join(stuff)) # turns stuff back from list into a string? (without CORN, which has been pop'd out)
print("#".join(stuff[3:5]))
# would it join some but not all of the items (telephone, light and sugar) with a # as the joinder? maybe not those items because of the pop on ln 21
# actually no, seems to work like range, in that the last one doesn't count