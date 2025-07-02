




# Programación orientada a objetos



La Programación Orientada a Objetos (POO) es un paradigma de programación que organiza el código en “objetos”, los cuales son como pequeños módulos que combinan datos y acciones relacionadas.

Es decir, en lugar de escribir todo el código suelto, creas plantillas llamadas "clases", y luego haces objetos que son instancias concretas de esas clases.


POO : Programación orientada a objetos
PARADIGMA :  Es un modelo de enfoque general apra pensar y organizar el desarrollo de software



Con POO buscamos :
* Modularidad
* Reusabilidad
* Facilidad de mantenimiento
* Abastracción 



####  CONCEPTOS CLAVES

# 1. ¿ Que es una CLASE ?

Una clase es una *plantilla, plano o molde que define* :
- Qué datos tiene un objeto (atributos)
- Qué puede hacer ese objeto(métodos o funciones)


class Perro:
    pass


# 2.¿.Cuando hablamos de instancia a que nos referimos ?

Una instancia es simplemente  un objeto concreto a partir de una clase.

# 3. ¿ Que es un OBJETO ?

- Es un ejemplar real creado a partir de una clase
- Cada objeto tiene sus propios valores

mi_perro = Perro() 
# Acá mi perro es un objeto( instancia) de la clase perro



# 4. ¿ Que son los ATRIBUTOS ?

- son las variables que *describen el estado o caracteristicas del objeto*
- Se suelen definir dentro del método especial __init__


class Perrro :
        def __init__(self,nombre,edad):
            self.nombre = nombre
            self.edad = edad


# Acá nombre y edad son atributos



# ¿ 5. Que son los métodos(funciones) ?
Un método es una función que está dentro de una clase y que describe las acciones o comportamiento que peude hacer un objeto.

def ladrar(self):
    print(f"{self.nombre} está ladrando")

# ladrar es un método


# 6. SELF

- Es una referencia al objeto propio
- Se usa para acceder a sus atributos y me´todos desde dentro de la clase


# 7 MÉTODO ESPECIAL __INIT__

- Es un constructor. se ejecuta automáticamente cuandoc reas un objeto
- Sirve para inicializar atributos

def __init__(self, nombre):
    self.nombre = nombre


# 8 . ¿ Que es INSTANCIAR ?

- Es el proceso de crear un objetio a partir de  una clase
- cada vez que haces

 mi_perro = Perro("michis")
 # Acá estas instanciando un objeto 
