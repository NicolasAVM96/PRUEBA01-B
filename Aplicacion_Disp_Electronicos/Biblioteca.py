class Biblioteca:
    def __init__(self, lista_materiales = []):
        self.lista_materiales = lista_materiales
        
    def agregar_material(self, material): #Funcion para agregar materiales a la lista
        self.lista_materiales.append(material)
        print(f"Se a agregado un material a la biblioteca")
        
    def mostrar_catalogo(self): #Recorre la lista del catalogo y suma el monto de los precios de cada material
        total = 0
        if self.lista_materiales:
            i = 0 #Variable encargada de enumerar los materiales 
            for material in self.lista_materiales:
                i += 1 #Se le suma 1 para partir desde el 1 en la enumeracion
                print(f"\n{i}.- {material.descripcion()}, Precio: ${material.get_precio()}clp")
                total += material.get_precio() #Se suman los precios de los materials
            print(f"\nTotal del valor de los material de la concesionaria: ${total}clp")
        else:
            print("No hay material agregados al catalogo. Porfavor agregue un material.")