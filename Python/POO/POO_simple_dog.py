

"""
Cada OBJETO es una instancia de una CLASE, 
que es una plantilla para crear objetos. 
Las clases encapsulan datos y comportamientos relacionados, 
lo que permite organizar el código de manera más estructurada y reutilizable.



OBJETO: Es una instancia de una clase( caracteristicas y comportamientos definidos), 
que contiene atributos (datos) y métodos (funciones) 
definidos en la clase. Los objetos son las entidades 
concretas que se crean a partir de las clases.
"""





# 1 DEFINIMOS LA PLANTILLA DE LA CLASSE

class Perro():

    # 2. DEFINIMOS LOS CONSTRUCTORES DE LA CLASE
    def __init__(self, nombre, edad, raza,peso, region) :
        self.nombre = nombre
        self.edad = edad  # ATRIBUTO
        self.raza = raza  #ATRIBUTO
        self.peso = peso  #ATRIBUTO
        self.region = region # ATRIBUTO

    # 3. DEFINIMOS LOS MÉTODOS DE LA CLASE
    def ladrar(self):
        return f"{self.nombre} esta ladrando"
    
    def correr(self):
        return f"{self.nombre} esta corriendo"
    
    def region_perro(self) :
        if self.region == "colombia":
            return f"{self.nombre} es de Colombia"
        elif self.region == "argentina":
            return f"{self.nombre} es de Argentina"
        else:
            return f"{self.nombre} es de otro país"
        

# 4. CREAR INSTANCIAS DE LA CLASE
perro1 = Perro("Firulais", 5, "Labrador", 30, "colombia")
perro2 = Perro("Rex", 3, "Pastor Alemán", 35, "argentina")

# 5. USAR LOS MÉTODOS DE LA CLASE
print(perro1.ladrar())  # Output: Firulais esta ladrando
print(perro2.correr())  # Output: Rex esta corriendo
print(perro1.region_perro())  # Output: Firulais es de Colombia
print(perro2.region_perro())  # Output: Rex es de Argentina
