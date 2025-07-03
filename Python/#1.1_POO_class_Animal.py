





#EJERCICIOS  PARA COMPRENDER EL TEMA AVANZADO

class Animal() :
    def __init__(self, nombre,edad):
        self.nombre = nombre 
        self.edad = edad
        self.__energia = 100 #ENCAPSULAMIENTO


    def dormir(self, horas):
        self.__energia += horas * 10
        return f"{self.nombre} durmió {horas}. energia ahora {self.__energia}"
    

    
    def Jugar(self,tiempo):
        if self.__energia >= tiempo * 5 :
            self.__energia -= tiempo * 5
            return f"{self.nombre} juego {tiempo} hora. energia ahora : {self.__energia}"
        else :
            return f"{self.nombre} está cansado, encesita descansar"
        


# Instancias un objeto

mi_gato = Animal("michi",12)
print(mi_gato.dormir(2))
print(mi_gato.Jugar(2))
print(mi_gato.Jugar(12))


# PREGUNTA PRINCIPALES PARA RESOLVER SOBRE EL PRESENTE CÓDIGO

#1 ¿ Por qué utilizamos el self y el __init__ al inicializar una variable ?

"""
SELF  es una referencia al propio objeto(instancia) que se está creando o usando.
- Sirve para acceder a sus propios atributos y métodos dentro de la clase.
- Es un puente entre el objeto creado y su definición de clase.

Cuando hacemos  :
mi_gato = Animal("Michi",12)

Python crea un objeto mi_gato.
Cada vez que llamas un método (mi_gato.dormir(2)) self es mi_gato por dentro

si no utilizamos self, estariamos usando una variable local que se pierde

Self seria el que atribuye la variable su argumento.
"""

#2 Porque al inicializar los atributos utilizamos __init__ ?

"""
__init__
Este es un método especial llamado constructor que tiene toda clase en python.

- Se ejecuta automáticamente cuando creas un objeto
- Sirve para inicializar los atributos del objeto, osea, darle su estado inicial

Es como el constructor de una casa : define cómo quedará cuando la construyas ( Cuántos, cuartos
color..etc.)

Ejemplo :
"""
class Animal :
    def __init__(self,nombre, edad) :
        self.nombre = nombre 
        self.edad = edad 

"""
cuando haces : 
mi_gato = Animal("michi", 12)

Automáticamente :
- creas un espacio de memoria para el objeto mi_gato
- Llama __init__ con esos valores 

"""

Animal.__init__(mi_gato,"michi", 12)
# por detrás self es mi_gato