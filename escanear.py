import yara
import os

# Cargar las reglas compiladas
rules = yara.load('/home/osboxes/Practica_Malware/reglas_yara/rules-compiled')

# Directorio de malware
malware_folder = '/home/osboxes/Practica_Malware/malware'

# Recorrer los archivos de malware
for root, dirs, files in os.walk(malware_folder):
    for filename in files:
        filepath = os.path.join(root, filename)
        try:
            matches = rules.match(filepath)
            if matches:
                print(f'Match encontrado en {filepath}: {matches}')
        except Exception as e:
            print(f'Error en archivo {filepath}: {e}')
