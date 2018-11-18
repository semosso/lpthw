from sys import argv # BRK: esquecer de IMPORT argv; es

script, user_name = argv # BRK: esquecer de fornecer argumento quando chamar no terminal
prompt = '> '

print(f'Hi {user_name}, I\'m the {script} script.') # BRK: take out \ before '
print('I\'d like to ask you a few questions.')
print(f'Do you like me {user_name}?')
likes = input(prompt)

print(f'Where do you live, {user_name}?')
lives = input(prompt)

print('What kind of computer do you have?')
computer = input(prompt)

print(f'''
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
''') # BRK: forget F in ln 7