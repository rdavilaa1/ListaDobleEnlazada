from graphviz import Digraph

class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido=apellido
        self.carnet=carnet
        self.siguiente = None
        self.anterior=None

class ListaDobleEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacia(self):
        return self.primero == None

    def agregar_final(self, nombre, apellido, carnet):
        if self.vacia():
            self.primero = self.ultimo = Nodo(nombre, apellido, carnet)
        else:
            aux = self.ultimo
            nuevo = Nodo(nombre, apellido, carnet)
            aux.siguiente = nuevo
            nuevo.anterior = aux
            self.ultimo = nuevo
        self.size += 1

    def agregar_inicio(self, nombre, apellido, carnet):
        if self.vacia():
            self.primero = self.ultimo = Nodo(nombre, apellido, carnet)
        else:
            nuevo = Nodo(nombre, apellido, carnet)
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo
        self.size += 1

    def recorrer_inicio(self):
        aux = self.primero
        while aux != None:
            print("Nombre:", aux.nombre)
            print("Apellido:", aux.apellido)
            print("Carnet:", aux.carnet)
            print("--------------------")
            aux = aux.siguiente

    def eliminar_por_carnet(self, carnet):
        if self.vacia():
            print("La lista está vacía")
            return

        aux = self.primero

        while aux != None:
            if aux.carnet == carnet:

                # opción único nodo
                if aux == self.primero and aux == self.ultimo:
                    self.primero = None
                    self.ultimo = None

                # opción primero
                elif aux == self.primero:
                    self.primero = aux.siguiente
                    self.primero.anterior = None

                # opción último
                elif aux == self.ultimo:
                    self.ultimo = aux.anterior
                    self.ultimo.siguiente = None

                # opción en medio
                else:
                    aux.anterior.siguiente = aux.siguiente
                    aux.siguiente.anterior = aux.anterior

                self.size -= 1
                print("Nodo eliminado correctamente")
                return

            aux = aux.siguiente

        print("No se encontró el carnet")

    def graficar(self):
        if self.vacia():
            print("La lista está vacía, no se puede graficar")
            return

        dot = Digraph(comment="Lista Doble Enlazada")
        dot.attr(rankdir="LR")

        aux = self.primero
        i = 0

        while aux != None:
            nombre_nodo = "Nodo" + str(i)
            etiqueta = f"{aux.nombre}\n{aux.apellido}\n{aux.carnet}"

            dot.node(nombre_nodo, etiqueta)

            if aux.siguiente != None:
                dot.edge(nombre_nodo, "Nodo" + str(i+1))
                dot.edge("Nodo" + str(i+1), nombre_nodo)

            aux = aux.siguiente
            i += 1

        dot.render("lista_doble_enlazada", format="png", view=True)
        print("Gráfica generada correctamente")

lista = ListaDobleEnlazada()

while True:
    print("\n--- MENÚ ---")
    print("1. Agregar al final")
    print("2. Agregar al inicio")
    print("3. Mostrar lista")
    print("4. Eliminar por carnet")
    print("5. Graficar lista")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        carnet = input("Carnet: ")
        lista.agregar_final(nombre, apellido, carnet)

    elif opcion == "2":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        carnet = input("Carnet: ")
        lista.agregar_inicio(nombre, apellido, carnet)

    elif opcion == "3":
        lista.recorrer_inicio()

    elif opcion == "4":
        carnet = input("Ingrese el carnet a eliminar: ")
        lista.eliminar_por_carnet(carnet)

    elif opcion == "5":
        lista.graficar()

    elif opcion == "6":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")
        
    