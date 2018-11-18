# Find something you need to calculate and write a new .py file that does it
# Golden rule calculator

M_age = 31
W_age = 25

# one alternative
print("Am I compliant with the golden rule?")
print(M_age / 2 + 7 < W_age)

# another alternative
print("Am I compliant with the golden rule?", M_age / 2 + 7 < W_age)

# ??
# se eu quiser imprimir o resultado em uma segunda linha, como retirar o espaço do início da segunda?
# Takai: usando sep=""
print("Am I compliant with the golden rule?\n", M_age / 2 + 7 < W_age, sep="")