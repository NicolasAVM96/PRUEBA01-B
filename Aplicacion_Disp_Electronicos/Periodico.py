from Material import Material

class Periodico(Material): #Herencia de Material
    def __init__(self, titulo, autor, precio, fecha_publicacion):
        super().__init__(titulo, autor, precio)
        self.fecha_publicacion = fecha_publicacion
        
    def descripcion(self):#Describe los atributos del material
        return f"Tipo: Periodico, Titutlo: {self.titulo}, Autor: {self.autor}, Fecha de publicación: {self.fecha_publicacion}"
        
 