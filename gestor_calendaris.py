import sqlite3
import os

# --- CONFIGURACIÓ INICIAL ---
carpeta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_db = os.path.join(carpeta_actual, 'meu_calendari.db')

def mostrar_menu():
    print("\n--- 📅 GESTOR DE CALENDARIS ---")
    print("1. Veure tots els calendaris")
    print("2. Crear un nou calendari")
    print("3. Sortir")
    return input("Tria una opció: ")


while True:
    opcio = mostrar_menu()

    if opcio == "1":
        # LLISTAR
        connexio = sqlite3.connect(ruta_db)
        cursor = connexio.cursor()
        cursor.execute("SELECT * FROM calendaris")
        files = cursor.fetchall()
        
        print("\nELS TEUS CALENDARIS:")
        for f in files:
            print(f"[{f[0]}] - {f[1]}")
        connexio.close()

    elif opcio == "2":
        # AFEGIR
        nom = input("Nom del nou calendari: ")
        connexio = sqlite3.connect(ruta_db)
        cursor = connexio.cursor()
        cursor.execute("INSERT INTO calendaris (nom) VALUES (?)", (nom,))
        connexio.commit()
        print(f"✅ '{nom}' guardat!")
        connexio.close()

    elif opcio == "3":
        print("Adéu! 👋")
        break 

    else:
        print("Opció no vàlida, torna-ho a provar.")