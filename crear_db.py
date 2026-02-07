import sqlite3
import os

# 1. Obtenir la ruta de la carpeta on està aquest fitxer .py
carpeta_actual = os.path.dirname(os.path.abspath(__file__))

# 2. Definir el nom del fitxer de la base de dades dins d'aquesta carpeta
ruta_base_dades = os.path.join(carpeta_actual, 'meu_calendari.db')

# Mostrem si l'usuari ja te la base de dades al dispositiu i li indiquem
if os.path.exists(ruta_base_dades):
    print("Ja tens la base de dades creada al teu dispositiu")
    exit()

print(f"--- INFO ---")
print(f"Carpeta del script: {carpeta_actual}") 
print(f"Fitxer que es crearà: {ruta_base_dades}")
print(f"------------")
    
try:
    # 3. Connectar (ara amb la ruta absoluta)
    connexio = sqlite3.connect(ruta_base_dades)
    cursor = connexio.cursor()

    # 4. Crear la taula
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS calendaris (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS esdeveniments    (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            data TEXT NOT NULL,
            hora TEXT NOT NULL,
            calendari_id INTEGER,
            FOREIGN KEY (calendari_id) REFERENCES calendaris(id)
        )
    ''')

    connexio.commit()
    connexio.close()
    print("Èxit: Base de dades creada correctament!")

except Exception as e:
    print(f"Error, algo ha anat malament: {e}")
    
    
    
"""
Normalment, quan executes un script, la "ruta de treball" (on es creen els fitxers) pot ser la carpeta de l'usuari o qualsevol altra, 

depenent de com estigui configurat el terminal del Visual Studio Code. Amb el nou codi hem fet servir la llibreria os (Operating System):

os.path.abspath(__file__): Això li diu a Python: "Busca la ruta completa d'aquest fitxer .py que estic executant ara mateix".

os.path.dirname(...): Això li diu: "D'aquesta ruta, queda't només amb la carpeta, ignora el nom del fitxer".

os.path.join(...): Això serveix per ajuntar la carpeta amb el nom del fitxer (meu_calendari.db) de forma segura, 

os.path.exists(...): Tu li dones una "adreça" (una ruta al teu disc dur) i ell et torna una de dues respostes:

True: "Sí, he trobat un fitxer o una carpeta en aquesta adreça".

False: "Aquí no hi ha res, l'adreça està buida"

"""