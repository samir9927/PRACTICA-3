class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class listaDeCompras:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def agregar_final(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
            self.primero.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.siguiente = self.primero

        lista.recorrer()

    def recorrer(self):
        print("------------------")
        print("LISTA DE PRODUCTOS")
        print("------------------")
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break
        print("------------------")
    def remover_inicio(self):
        if self.vacia():
            print("Lista vacía")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.ultimo.siguiente = self.primero

        lista.recorrer()



try:
    if __name__ == "__main__":
        opcion = 0
        lista = listaDeCompras()
        while opcion != 4:
            print("--- Lista de Compras ---\n 1. Agregar Producto\n 2. Eliminar Producto\n 3. Salir de Lista")
            opcion = int(input("Ingrese su opción "))

            if opcion == 1:
                dato = input("Ingresa Producto: ")
                lista.agregar_final(dato)
            elif opcion == 2:
                lista.remover_inicio()
            elif opcion == 3:
                print("Adiós")
            else:
                print("Ingresaste una opción errónea, vuelve a intentarlo.")
except Exception as e:
    print(e)