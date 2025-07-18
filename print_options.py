# Imprimir un texto directamente
print("Hola Mundo")

# Imprimir el contenido de una variable
saludo = "Bienvenido al curso de Python"
print(saludo)

nombre = "Ana"
edad = 28

# Python añade un espacio automáticamente entre los valores
print("Nombre:", nombre, "| Edad:", edad)
# Salida: Nombre: Ana | Edad: 28

print("monitor", "teclado", "ratón", "camara", sep=" | ", end=" ***\n")
# Salida: monitor | teclado | ratón

# Por defecto, se imprime en líneas separadas
print("Procesando archivos...")
print("Completado.")

# Usando end=" " para continuar en la misma línea
print("Procesando archivos...", end=" ")
print("Completado.")
# Salida: Procesando archivos... Completado.

frase = "Solo soy un texto"
autor = "String"
a, b, c, d, e = 5, 8, 1, 5, 9

print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}")

# Sintaxis: poner una 'f' antes de las comillas y las variables entre {}
print(f"Frase: {frase}, Autor: {autor}", "AAAAA", sep='-')
# Salida: Frase: Solo soy un texto, Autor: String

valor = 3.14159
print(f"El valor de PI con dos decimales es: {valor:.2f}")
# Salida: El valor de PI con dos decimales es: 3.14

texto = "Python"

# Alinea el texto a la derecha en un espacio de 10 caracteres, rellenando con '-'
print(f"|{texto:->9}|")  # Salida: |----Python|
print(f"|{texto:-<9}|")  # Salida: |----Python|

# Alinea al centro en un espacio de 10
print(f"|{texto:-^9}|")  # Salida: |--Python--|

numero_grande = 1234567890

print(f"Número formateado: {numero_grande:,d}")
# Salida: Número formateado: 1,234,567,890

# También puedes usar '_' como separador
print(f"Número formateado: {numero_grande:_d}")
# Salida: Número formateado: 1_234_567_890

print("Primera línea\nSegunda línea")
print("\tEste texto está indentado.")
print('Para usar comillas simples dentro de comillas simples, debes \'escaparlas\'.')

# Forma tradicional (propensa a errores)
print("Ruta: C:\\Users\\Usuario\\Desktop")

# Forma moderna y segura con raw string (r"...")
print(r"Ruta: C:\Users\Usuario\Desktop")