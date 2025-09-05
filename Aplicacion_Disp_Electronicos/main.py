from Biblioteca import Biblioteca
from Funcion_menu import * #Se importan las funciones del menu

def menu():
    print("Bienvenido al Menu principal")
    biblio = Biblioteca([]) #Se instancia la biblioteca con una lista vacia
    salir_menu = False
    while not salir_menu:
        print(""" 
            === Menú Principal ===
            1. Agregar material al catalogo
            2. Mostrar catalogo
            3. Actualizar precio de un material
            4. Salir
            """)
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            agregar_material(biblio)
        elif opcion == "2":
            mostrar_catalogo(biblio)        
        elif opcion == "3":
            recorrer_actualiza_precio(biblio)        
        elif opcion == "4":
            salir_menu = salir()
        else:
            print("Ingrese una respuesta valida.")      

def salir():
    print("Adios!")
    return True

menu()