import sqlite3
import os


# --- CONFIGURACIÓ INICIAL ---
carpeta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_db = os.path.join(carpeta_actual, 'meu_calendari.db')
connexio = sqlite3.connect(ruta_db)
cursor = connexio.cursor()

# Ho posem tot en funcions llogiques per una millor organitzacio ara i futura

def mostrar_menu():
    print("\n\n---  GESTOR DE CALENDARIS ---")
    print("1. Veure tots els calendaris")
    print("2. Crear un nou calendari")
    print("3. Menu esdeveniments")
    print("4. Sortir")
    return input("\nTria una opció: ")

def mostrar_menu_esdeveniments():
    print("\nOpcions:")
    print("1. Veure esdeveniments d'un calendari")
    print("2. Crear nou esdeveniment")
    print("3. Tornar al menú principal\n")
    return input("Tria una opció: ")

def llistar_els_calendaris():
    cursor.execute("SELECT * FROM calendaris")
    return cursor.fetchall()        

def afegir_calendari(nom):
    cursor.execute("INSERT INTO calendaris (nom) VALUES (?)", (nom,))
    connexio.commit()
    return

def Hi_ha_esdeveniments():
    cursor.execute("SELECT calendari_id FROM esdeveniments")
    Hi_ha_esdeveniments_pregunta = cursor.fetchall()
    return Hi_ha_esdeveniments_pregunta

def Veure_esdeveniments(id_calendari):
    cursor.execute("SELECT * FROM esdeveniments WHERE calendari_id = (?)", (id_calendari,))
    esdeveniments = cursor.fetchall()
    return esdeveniments
    

while True:
   
    opcio = mostrar_menu()
    
    if opcio == "1":
        llista = llistar_els_calendaris()
        if not llista:
            print("\nNo tens cap calendari creat encara.")
            input("\nEnter per continuar")
        else:
            print("\nELS TEUS CALENDARIS:")
            for f in llista:
                print(f"[{f[0]}] - {f[1]}")
            input("\nEnter per continuar")         
        
    elif opcio == "2":
        nom = input("\nNom del nou calendari: ")  
        afegir_calendari(nom)   
        print(f"\n'{nom}' guardat!")
        input("\nEnter per continuar")

    elif opcio == "3":
        while True:
            opcio_calendari = mostrar_menu_esdeveniments()
            
            if opcio_calendari == "1":    
                if not Hi_ha_esdeveniments():
                    print("\nEncara no tens cap calendari o esdeveniments per veurels")
                    input("\nEnter per continuar")
                                       
                else:
                    id_calendari = input("\nNumero del calendari d'on vols veure els esdeveniments: ")    
                    for e in Veure_esdeveniments(id_calendari):
                        print(f"\n[{e[0]}]- {e[1]} el {e[2]} a les {e[3]}")
                        input("\nEnter per continuar")
                    
            elif opcio_calendari == "2":
                3
                cursor.execute("SELECT id FROM calendaris")
                Hi_ha_calendari = cursor.fetchall()
                    
                if not Hi_ha_calendari:
                    print("\nEncara no tens cap calendari on puguis crear els esdeveniments, primer crea un calendari i despres podras crear un esdeveniments")
                    input("\nEnter per continuar")
                    
                else:
                    
                    while True:
                        id_calendari = input("Numero del calendari on vols afegir l'esdeveniment: ")
                        
                        cursor.execute("SELECT id FROM calendaris WHERE id = ?", (id_calendari))
                        Existeix_id = cursor.fetchone()
                        
                        if Existeix_id == None:
                            
                            print("Aquet calendari no existeix")
                            input("\nEnter per continuar")
                            
                        else:                    
                            nom_esdeveniment = input("Nom de l'esdeveniment: ")
                            data_esdeveniment = input("Data: ")
                            hora_esdeveniment = input("Hora: ")
                                
                            cursor.execute(
                                "INSERT INTO esdeveniments (nom, data, hora, calendari_id) VALUES (?, ?, ?, ?)", 
                                (nom_esdeveniment, data_esdeveniment, hora_esdeveniment, id_calendari)
                                )
                            connexio.commit()
                            print(f"Esdeveniment '{nom_esdeveniment}' afegit al calendari ID {id_calendari}!")
                            input("\nEnter per continuar")
                            break
                    
            if opcio_calendari == "3":
                    break
         
    elif opcio == "4":
        print("\nAdéu!")
        connexio.close()
        break 

    else:
        print("\nOpció no vàlida, torna-ho a provar.")      
        input("\nEnter per continuar")