# Single equal (=) attributes name "cars" to data "100"
# In Zed's words: "assigns the value on the right to the variable on the left"
# Double equal (==) tests if two things are equal
cars = 100
# Attrivutes the name "space_in_a_car" to the data "4"
# You can do space_in_a_car=4 with no space between variable, equal, data; but that's bad form
space_in_a_car=4
# Attributes the name "drivers" to the data 30
drivers = 30
# Attributes the name "passengers" to the data 90
passengers = 90
# Calculates number of cars minus number of drivers, and attributes the name "cars_not_driven" to the result; below are the same
cars_not_driven = cars - drivers
# Attributes the name cars_driven to the data that drivers refers to
cars_driven = drivers
# Attributes the name carpool_capacity to the the data that is the result of the calc
carpool_capacity = cars_driven * space_in_a_car
# Attributes the name average_passengers_per_car to the data that is the result of the calc
average_passengers_per_car = passengers / cars_driven

print('There are', cars, 'cars available.')
print('There are only', drivers, 'drivers available.')
print('There will be', cars_not_driven, 'empty cars today.')
print('We can transport', carpool_capacity, 'people today.')
print('We have', passengers, 'to carpool today.')
print('We need to put about', average_passengers_per_car, 'in each car.')