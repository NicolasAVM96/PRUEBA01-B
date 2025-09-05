class Material:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo 
        self.autor = autor
        self.__precio = precio
        
    
    def get_precio(self): #Retorna el precio del material
        return self.__precio
    
    def set_precio(self, nuevo_precio):#Modifica el precio siempre y cuando el precio sea mayor a 0
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
            print(f"""Se a modificado el precio del materia.
                  Su precio actual es: ${self.__precio}clp""")
        else:
            raise ValueError("El precio debe ser mayor a 0.")
    
    def descripcion(self):#Describe los atributos del material
        return f"Titutlo: {self.titulo}, Autor: {self.autor}"
        

