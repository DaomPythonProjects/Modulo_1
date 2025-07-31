# Suma o Adición el operador tambien es usado para concatenar
# result = 12 + 3 + 5 # 20
# result = result + 3 # 23
# result = 12.6 + 45.12 + 12 # 69.72
# result = 12.5 + 34 + "18" # Error
# result = "18" + "15" # 1815
# num = str(12)+"12"
# print(num)
import math

# Resta o Substraccion
# resta = 10 - 5 - 7 # -2
# resta2 = resta - 3 # -5
# result = 12.6 - 45.12 - 12 #
# # result = 12.5 - 34 - "18" # Error
# # result = "18" - "15" # Error
# x = max(1, 10 - 15) # Forzar un minimo para la resta (x = 0)
# print(x)

# Multiplicacion el operador tambien es usado para multiplicar cadenas
# num = 3 * 3 * 2
# num2 = num * 2
# num = 12.6 * 45.12 * 12
# # result = 12.5 * 34 * "18" # Error
# # result = "18" * "15" # Error
# result = "18" * 3 # 181818 (cadena * n)
# result = "ja " * 3 + "mes" # ja ja ja mes
# x = abs(-5) * 3 # Forzar resultado positivo
# print(x)

# Division
# num = 18 / 2 / 2
# num2 = num / 2
# num = 12.6 / 1.1 / 2
# # result = 120.5 / 1.2 / "18" # Error
# # result = "18" / "15" # Error
# # result = "18" / 3 # Error
# x = abs(-5) / 2 # Forzar resultado positivo
# print(x)
# print(divmod(7, 3)) # 7 / 3 obteniendo cociente y resto (2,1)
# print(round(5 / 2)) # redondear a un entero (2)

# Potenciacion
# num = 2 ** 3 ** 2 #
# num2 = num ** 4 # 6561
# num = 12.6 ** 1.1 ** -2 # 8.117029880977896
# # result = 12.5 ** 2 ** "18" # Error
# x = abs(-5) ** 3 # Forzar resultado positivo 125

# Division entera
num = 19 // 2 # 9

# Modulo
num = 19 % 2 % 2 # 1
num = 12.6 % 3 # 0.599
# result = 120.5 % "2" # Error
x = abs(-120.5) % 2 # resultado distinto 0.5
x = -120.5 % 2 # Forzar resultado positivo 1.5
print(x)