"""
--- GUIA RÀPIDA DE SQLITE3 ---

1. .cursor()
   És com un "punter" o un "obrer" que enviem a la base de dades. 
   La connexió obre la porta del fitxer, però el cursor és qui 
   executa les ordres (execute) i qui ens porta els resultats.

2. .execute("ORDRE SQL", (paràmetres,))
   Serveix per enviar una ordre a la base de dades. 
   Sempre usem '?' per seguretat en lloc de variables directes.

3. .fetchall()
   S'usa després d'un SELECT. Recupera TOTES les files que ha trobat 
   la consulta i les guarda en una llista de Python.
   Cada fila de la llista és una 'tupla' (com una llista que no es pot canviar).

4. .fetchone()
   Igual que fetchall, però només ens porta la primera fila que trobi.

5. .commit()
   Molt important! Si fas canvis (INSERT, UPDATE, DELETE), 
   els canvis no es guarden al disc dur fins que no fas .commit().
   És com prémer el botó "Guardar" del Word.
"""



import sqlite3
import os

# --- CONFIGURACIÓ INICIAL ---
carpeta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_db = os.path.join(carpeta_actual, 'meu_calendari.db')
connexio = sqlite3.connect(ruta_db)
cursor = connexio.cursor()

def mostrar_menu():
    print("\n---  GESTOR DE CALENDARIS ---")
    print("1. Veure tots els calendaris")
    print("2. Crear un nou calendari")
    print("3. Sortir")
    return input("Tria una opció: ")


def mostrar_menu_calendari():
    print("\nOpcions:")
    print("1. Veure esdeveniments d'un calendari")
    print("2. Crear nou esdeveniment")
    print("3. Tornar al menú principal")
    return input("Tria una opció: ")


while True:
    opcio = mostrar_menu()

    if opcio == "1":
        # LLISTAR
        
        cursor.execute("SELECT * FROM calendaris")
        files = cursor.fetchall()
        
        print("\nELS TEUS CALENDARIS:")
        for f in files:
            print(f"[{f[0]}] - {f[1]}")
        
        while True:
            
            opcio_calendari = mostrar_menu_calendari()
            
            if opcio_calendari == "1":
                id_calendari = input("\nID del calendari que vols veure: ")
                cursor.execute("SELECT * FROM esdeveniments WHERE calendari_id = (?)", 
                               (id_calendari,)
                )
                
                esdeveniments = cursor.fetchall()
                for e in esdeveniments:
                    print(f"\n[{e[0]}]- {e[1]} el {e[2]} a les {e[3]}")
                
            if opcio_calendari == "2":
                id_calendari = input("ID del calendari on vols afegir l'esdeveniment: ")
                nom_esdeveniment = input("Nom de l'esdeveniment: ")
                data_esdeveniment = input("Data: ")
                hora_esdeveniment = input("Hora: ")
                
                cursor.execute(
                    "INSERT INTO esdeveniments (nom, data, hora, calendari_id) VALUES (?, ?, ?, ?)", 
                    (nom_esdeveniment, data_esdeveniment, hora_esdeveniment, id_calendari)
                )
                connexio.commit()
                print(f"Esdeveniment '{nom_esdeveniment}' afegit al calendari ID {id_calendari}!")
                
            if opcio_calendari == "3":
                break
            
                
    elif opcio == "2":
        # AFEGIR
        nom = input("Nom del nou calendari: ")
        cursor.execute("INSERT INTO calendaris (nom) VALUES (?)", (nom,))
        connexio.commit()
        print(f"'{nom}' guardat!")

    elif opcio == "3":
        print("Adéu!")
        connexio.close()
        break 

    else:
        print("Opció no vàlida, torna-ho a provar.")      