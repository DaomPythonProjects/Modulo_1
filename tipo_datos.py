palabra_original = "dabale arroz a la zorra el abad" # 5 Caracteres
palabra = palabra_original.replace(" ", "") # Elimina los espacios en blanco

# print(f'Tu nombre es: {mi_nombre}')
# print(type(m i_nombre))
# print(f"El caracter es: {mi_nombre[1]}") # Salida: D
invertido = "" # Variable para almacenar el texto invertido
for i in range(len(palabra) - 1, -1, -1): # 0 hasta 4
    invertido = invertido + palabra[i]

if invertido == palabra:
    print(f"{palabra_original} es un palíndromo")
else:
    print(f"{palabra_original} no es un palíndromo")


name = "Diego"
last_name = "Ojeda"

# Usando f-strings (Recomendado)
template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3', template)

# Métodos más antiguos
template = ("Hola, mi nombre es {} y mi apellido es {}, mi edad es {}"
            .format(name, last_name, 48))
print('v2', template)

# No recomendado, pero aún funcional
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1 ', template)

# Multiplicación
#saludo = "Ja " * 3 + 'mes'  # 'Ja Ja Ja mes'
saludo = f"{'Ja ' * 3}James"  # 'Ja Ja Ja mes'
print(saludo)

# Cadenas "Raw" para anular caracteres de escape (útil en rutas de Windows)
ruta = r'C:\Users\name'
print(ruta)

# Cadenas multilínea con triples comillas
mensaje_largo = """Esto es un mensaje
que ocupa varias
líneas."""
print(mensaje_largo)

Enteros
vidas = int(3_122 / 3)
vidas -= 1 # Operador de asignación compuesta
print(vidas) # Salida: 9
print(f"{vidas:_d}")  # Salida: El número de vidas es: 123,122,537
print(type(vidas))

# Flotantes
temperatura = 12.12
print(f'Mi temperatura es: {temperatura}') # Salida: Mi temperatura es: 12.12
temperatura *= 3
print(type(temperatura)) # Salida: <class 'float'>

# Notación científica para números muy grandes o pequeños
presupuesto = 1.5e6 # 1.5 * 10^6 = 1,500,000.0
print(presupuesto)

# Complejos
z = 3j * 2j
print('Z =>', z)
print(type(z)) # Salida: <class 'complex'>
print(f"Parte real: {z.real}, Parte imaginaria: {z.imag}")

# Booleanos
esta_activo = True
print('Activo? ', esta_activo )
print(type(esta_activo ))
print(not esta_activo) # Negacion Salida: False

var = bool(1)
print(var)

var = bool("1")
print(var)  # Salida: True, porque cualquier cadena no vacía es True

var = bool(None)
print(var)

# Castear a string
numero_como_cadena = str(123) # "123"

# Castear a entero
cadena_a_entero = int("45") # 45

# Castear a float
entero_a_float = float(10) # 10.0

# Castear a booleano
numero_a_booleano = bool(0) # False

resultado = bool(not str(int([True,False,True][2])))
print(resultado)