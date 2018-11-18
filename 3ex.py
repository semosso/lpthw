print("I will now count my chickens:")

print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)
# o que chega antes de % é 75 (100 - 25 * 3); o resultado de 75 % 4 é 3 (resto de 75 / 4)

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
# % means module (i.e., resto da divisão); o que chega antes de % é 5 (3+2+1-5+4); o resultado de 5 % 2 é 1 (resto de 5 / 2)

print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)
# se não houvesse o < (ou melhor, se fosse um outro sinal matemático, + - / *), ele printaria um número

print("What is 3 + 2?", 3 + 2) # poderia juntar ln 12 e 13 em uma só fazendo algo parecido; teste em ln 27
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more?")

print("Is it greater?", 5 > -2)
print("Is it greater or egual?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)

print("Is it true that 3 + 2 < 5 - 7?", 3 + 2 < 5 - 7)
print("Is it true that 3 + 2 < 5 - 7?",3 + 2 < 5 - 7) # printa a mesma coisa que ln 27, mesmo sem o espaço entre , e operação