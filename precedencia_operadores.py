resultado = 10 + 3 * 2 ** 2 # ¿Cuál es el resultado?
print(resultado)

# 1. Potenciación (**)
# resultado = 10 + 3 * 4

# 2. Multiplicación (*)
# resultado = 10 + 12

# 3. Suma (+)
# resultado = 22

# 1) Paréntesis y corchetes/llaves (listas, diccionarios/sets)
# 2) Indización, rebanado, llamada y referenciación de atributos.
# 3) Expresión await
# 4) Exponenciación (**)
# 5) Complemento/or binario, mas y menos unitarios ~ + -
# 6) Multiplicación división, módulo, división entera y multiplicación de matrices (* / % // @)
# 7) Suma y resta (+ -)
# 8) Desplazamiento bit a derecha e izquierda (>> <<)
# 9) AND binario (&)
# 10) XOR (OR exclusivo) binario (^)
# 11) OR binario (|)
# 12) Operadores de comparación (<= < > >=), operadores de igualdad (== !=) operador de pertenencia (in) y de identidad (is)
# 13) NOT lógico
# 14) AND lógico
# 15) OR lógico
# 16) Operadores de asignación (= %= /= //= -= += *= **= :=)

x = 10
y = x * 3 - 3 ** 10 - 2 + 3

# Distinto
x = 10
y = (x*3-3)**(10-2)+3
print(f"resultado: {y:,d}")  # Salida: resultado: -59049.00

# Metodo PEMDAS
print(2 ** 3 + 3 - 7 / 1 // 4)
"""
P = paréntesis ()
E = exponentes
M = multiplicación
D = división
A = adicción
S = sustración
"""

print(2 ** 3)
print((7 / 1) // 4)

print(8 + 3 - 1)