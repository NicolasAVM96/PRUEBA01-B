from Material import Material

class Libro(Material): #Herencia de Material
    def __init__(self, titulo, autor, precio, paginas = 0):
        super().__init__(titulo, autor, precio)
        self.paginas = paginas
        
    def descripcion(self):#Describe los atributos del material
        return f"Tipo: Libro, Titutlo: {self.titulo}, Autor: {self.autor}, Numero de paginas: {self.paginas}"
    
