from Libro import Libro
from Revista import Revista
from Periodico import Periodico

def agregar_material(biblio): #Funcion que instancia un material: libro, revista, periodico. / Llama a la funcion mmp
    print(""" 
        === Elija un tipo de material que quiera agregar ===
        1. Libro
        2. Revista
        3. Periodico
        4. Volver al menu principal
        """)
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        titulo, autor, precio = mmp()
        paginas = validar_numero((input("Ingrese el numero de paginas del libro: ")))
        libro = Libro(titulo, autor, precio, paginas)#Instancia un libro
        biblio.agregar_material(libro)
    elif opcion == "2": 
        titulo, autor, precio = mmp()
        edicion = validar_numero((input("Ingrese la edicion de la revista: ")))
        revista = Revista(titulo, autor, precio, edicion)#Instancia una revista
        biblio.agregar_material(revista)
    elif opcion == "3": 
        titulo, autor, precio = mmp()
        fecha_publicacion = input("Ingrese la fecha de publicacion del periodico (DD/MM/YYYY): ")
        periodico = Periodico(titulo, autor, precio, fecha_publicacion)#Instancia un preiodico
        biblio.agregar_material(periodico)
    elif opcion == "4":
        return 
    else:
        print("Eliga una de las opciones correctas")
        
def mmp(): #Se consulta sobre titulo, autor y Precio
    titulo = input("Ingrese la titulo del material: ")
    autor = input("Ingrese el autor del material: ")
    precio = validar_numero((input("Ingrese el precio del material (CLP): ")))
    return titulo, autor, precio

def mostrar_catalogo(biblio): #Funcion que llama a la funcion mostrar_catalogo()
    biblio.mostrar_catalogo()

def recorrer_actualiza_precio(biblio): #Recorre la lista de materiales y selecciona una opcion
    biblio.mostrar_catalogo() #Mostramos el catálogo de materiales
    if not biblio.lista_materiales:
        print("No hay vehículos en la lista.")
        return
    while True: #Pedimos un numero del material y validamos que esté dentro del rango
        opcion = validar_numero(input("\n=== Ingrese el número del material para modificar su precio ===\nOpción: "))
        if 1 <= opcion <= len(biblio.lista_materiales):
            nuevo_precio = validar_numero((input("\nIngrese un nuevo precio para el material: ")))
            biblio.lista_materiales[opcion-1].set_precio(nuevo_precio) #Se actualiza el precio en el material seleccionado 
            break
        else:
            print(f"Opción inválida. Seleccione un numero de la lista.")
    
def validar_numero(numero): #Valida si el numero ingresado es int
    while True:
        try:
            numero = int(numero)
            return numero
        except ValueError:
            numero = input("Entrada inválida. \nPor favor, ingrese un numero valido: ")
