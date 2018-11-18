# Combine escape sequences and FORMAT function
liters = 2
protein = 'red meat'
salad = 'sweet lettuce'
beverage = f'{liters} liters of apple juice'
sweets = 'alfajor'

print('Shopping list:\n\t- {}\n\t- {}\n\t- {}\n\t- {}'.format(
    protein,
    salad,
    beverage,
    sweets
))

# why doesn't ln 25 work?
liters = 2
protein = 'red meat'
salad = 'sweet lettuce'
beverage = '{liters} liters of apple juice'
sweets = 'alfajor'

print('Shopping list:\n\t- {}\n\t- {}\n\t- {}\n\t- {}'.format(
    protein,
    salad,
    beverage.format(liters),
    sweets
))