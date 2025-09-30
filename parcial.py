#Damian Bermudez Lara

class Persona:

    def __init__(self, nombre, apellido, edad, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.telefono = telefono

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"correo: {self.correo}")
        print(f"telefono: {self.telefono}")
        print("-" * 40)


class registro:
    def __init__(self):
        self.preguntas = ["¿Cuál es o son tus nombres?","¿cual es o son tus apellidos?","¿cuantos años tienes?","¿cual es tu correo electronico?","¿cual es tu numero de contacto?"] 
        self.respuestas = []        
    
    def realizar_registro(self):
        print("Bienvenido al registro. Por favor, responde las siguientes preguntas:")
        for i in self.preguntas:
            respuesta = input(f"{i}")
            self.respuestas.append(respuesta)
        persona = Persona(
            nombre=self.respuestas[0],
            apellido=self.respuestas[1],
            edad=self.respuestas[2],
            correo=self.respuestas[3],
            telefono=self.respuestas[4]
        )
        return persona
     
        
    def mostrar_info(self):
        print("\n Aquí están tu informacion: \n")
        for i in self.respuestas:
            print(f"Respuesta: {i}\n")

class libros:
    def __init__(self, nombre, categoria):
        self.nombre=nombre
        self.categoria =categoria
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"categoria: {self.categoria}")



class registro_libro:
    def __init__(self):
        self.preguntas = ["¿Cuál es el nombre del libro?","¿cual es la categoria del libro?"]
        self.respuestas = []        
    
    def realizar_registro(self):
        print("Bienvenido al registro de libros. Por favor, responde las siguientes preguntas:")
        for i in self.preguntas:
            respuesta = input(f"{i}")
            self.respuestas.append(respuesta)
        libro = libros(
            nombre=self.respuestas[0],
            categoria=self.respuestas[1]
        )
        return libro
    def mostrar_info(self):
        print("\n Aquí están tu informacion: \n")
        for i in self.respuestas:
            print(f"Respuesta: {i}\n")

print("bienvenido a la biblioteca \n")
print("presiona 1 para registrarte como usuario \n")
print("presiona 2 mostrar personas registradas \n")
print("presiona 3 para registrar libros \n")
print("presiona 4 mostrar los libros registrados\n")
print("presiona 0 para salir \n")

def main():

    menu = int(input("que opcion selecionas ---------> "))

    personas_registradas = []
    libros_registrados = []

    while menu != 0 :
        if menu == 1:
            print(f"\n registro")
            registrar = registro()
            persona = registrar.realizar_registro()
            personas_registradas.append(persona)
        elif menu == 2:
            print("\n personas registradas:")
            for i in personas_registradas:
                i.mostrar_info()
        elif menu == 3:
            print(f"\n registro")
            registrar_libro = registro_libro()
            libro = registrar_libro.realizar_registro()
            libros_registrados.append(libro)
        elif menu == 4:
            print("\n libros registrados:")
            for i in libros_registrados:
                i.mostrar_info()
        menu = int(input("que opcion selecionas ---------> "))

if __name__ == "__main__":
    main()
    