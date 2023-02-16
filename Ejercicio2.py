class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaDeTareas:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.primero.siguiente = self.primero
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux
            self.ultimo.siguiente = self.primero
        lista.recorrer()

    def recorrer(self):

        print("------------------")
        print("LISTA DE TAREAS")
        print("------------------")
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break
        print("------------------")

    def remover_final(self):
        if self.vacia():
            print("Lista vacía")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            aux = self.primero
            while aux.siguiente != self.ultimo:
                aux = aux.siguiente
            aux.siguiente = self.primero
            self.ultimo = aux
        lista.recorrer()

try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaDeTareas()
        while opcion != 3:
            print("--- Lista de Tareas ---\n 1. Agregar Tarea\n 2. Eliminar Tarea\n 3. Salir")
            opcion = int(input("Ingrese su opción "))

            if opcion == 1:
                dato = input("Ingresa tarea: ")
                lista.agregar_inicio(dato)            
            elif opcion == 2:
                lista.remover_final()
            elif opcion == 3:
                print("Adiós")
            else:
                print("Ingresaste una opción errónea, vuelve a intentarlo.")
except Exception as e:
    print(e)
