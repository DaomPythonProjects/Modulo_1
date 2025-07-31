a = [1, 2, 3]
b = a
c = [1, 2, 3]

var = a is b  # True, b es solo otro nombre para el mismo objeto lista
print(var)
var = a is c  # False, son dos objetos diferentes, aunque contengan los mismos valores
print(var)
c = a # Ahora c es una referencia al mismo objeto que a
print(a == c) # True, sus valores son iguales

print('a' in 'Naranja') # True
print('z' not in 'Naranja') # True
print(5 in [1, 2, 3, 4]) # False