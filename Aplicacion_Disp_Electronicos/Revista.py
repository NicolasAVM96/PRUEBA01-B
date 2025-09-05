from Material import Material

class Revista(Material): #Herencia de Material
    def __init__(self, titulo, autor, precio, edicion = 0):
        super().__init__(titulo, autor, precio)
        self.edicion = edicion
        
    def descripcion(self): #Describe los atributos del material
        return f"Tipo: Revista, Titutlo: {self.titulo}, Autor: {self.autor}, Edición: {self.edicion}"
        
