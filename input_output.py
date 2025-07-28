nombre = input("Ingresa tu nombre: ")
print(f"Hola, {nombre}!")

edad_str = input('Cual es tu edad? ')
print(f"{type(edad_str)}") # <class 'str'>

# Es crucial convertir la cadena a un número para hacer cálculos
edad_num = int(edad_str)
print(f"Tu edad es {edad_num}. El próximo año tendrás {edad_num + 1}.")
print(f"El tipo de dato es: {type(edad_num)}")

resultado = 42
print(f"El resultado es: {resultado}")

# Ejemplo con f-strings (recomendado)
year = 2022
event = "Elecciones"
print(f"Resultados de las {year} {event}")

# Ejemplo con el mini-lenguaje de formato
yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
# Usando f-string para el mismo formato complejo:
print(f"{yes_votes:.>6} YES votes   {percentage:2.2%}")