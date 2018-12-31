# creating a mapping of state to abbreviation
states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}

# create a basic set of states and some cities in them
cities = {
    "CA": "San Francisco",
    "MI": "Detroit",
    "FL": "Jacksonville"
}

# add some more cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

# print out some cities
print("-" * 10)
print("NY State has: ", cities["NY"])
print("OR State has: ", cities["OR"])

# print some states
print("-" * 10)
print("Michigan's abbreviation is: ", states["Michigan"])
print("Florida's abbreviation is: ", states["Florida"])

# do it by using the state then cities dict
print("-" * 10)
print("Michigan has: ", cities[states["Michigan"]])
print("Florida has: ", cities[states["Florida"]])

# print every state abbreviation
print("-" * 10)
for state, abbrev in list(states.items()): # calling LIST function (i.e., turns into list), which parameter is the result of calling method ITEMS on dict STATES
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print("-" * 10)
for abbrev, city in list(cities.items()): # same explanation as ln 38; with no .items method, list(dict) returns only keys; .items returns both key and values (see ln 51)
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print("-" * 10)
for state, abbrev in list(states.items()): # from Python doc: items() "Returns a new view of the dictionary’s items ((key, value) pairs)."
    print(f"{state} is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print("-" * 10)
# safely get a abbreviation by state that might not be there
state = states.get("Texas") # is GET how you call the item associated with the key?

if not state:
    print("Sorry, no Texas")

# get a city with a default value
city = cities.get("TX", "Does not exist") # does this mean "if you can't get because it's not there, assign "does not exist" to city"? 
print(f"The city for the state \"TX\" is: {city}")

# STUDY DRILLS
# understand how these are all different

print(list(states)) # no method returns only keys
print(list(states.values())) # .values() returns values
print(list(states.items())) # .items() returns both keys and values