import subprocess # Módulo moderno y recomendado

# Ejecutar un comando simple en la consola (en Linux/Mac)
# En Windows, sería: subprocess.run(['cmd', '/c', 'dir'])
resultado = subprocess.run(['ls', '-1', '*.py'], capture_output=True, text=True)

# Podemos inspeccionar la salida capturada
print("Archivos de Python:\n", resultado.stdout)

resultado = subprocess.run(['ls', '-1', '*.md'], capture_output=True, text=True)

print("Archivos de MD:\n", resultado.stdout)

import os # Libreria para obtener acceso al S.O (Archivos, Rutas, EOL)

# Ejecutar un comando simple en la consola
os.system('echo Hello, World!')

# Crear un directorio
os.system('mkdir new_directory')

# Listar los archivos en el directorio actual
os.system('ls')  # En Windows, usa 'dir' en lugar de 'ls'

# Ejecutar un programa externo (en este caso, abrir el bloc de notas en Windows)
os.system('notepad')  # En Linux/Mac, puedes usar 'gedit' o cualquier otro editor de texto

# Obtener una variable del sistema
print("Hola, esto es python", 12+5, " ", 10-5, 2*3, 8/2, sep=os.linesep)