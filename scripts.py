import subprocess
import sys

for line in sys.argv[1:]:
    subprocess.run(['mkdir', line], capture_output=True, text=True)

subprocess.run(['explorer', sys.argv[1]], capture_output=True, text=True)
print("Carpeta creada:", sys.argv[1])

# sys.argv es una lista de cadenas de texto con los argumentos
# 1. Validar que se pasaron suficientes argumentos
if len(sys.argv) < 3:
    print(f"Error: Debes proporcionar dos números.", file=sys.stderr)
    print(f"Uso: python {sys.argv[0]} <numero1> <numero2>", file=sys.stderr)
    sys.exit(1) # Termina el script con un código de error

# 2. Los argumentos son cadenas, hay que convertirlos a números
try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print(f"La suma de los números es: {num1 + num2}")
except ValueError:
    print("Error: Ambos argumentos deben ser números enteros.", file=sys.stderr)