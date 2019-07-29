class nodo:
    def __init__(self, dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente

class lista:
    def __init__(self):
        self.cabeza = None
    
    def insertar(self, dato):
        auxinsertar = nodo(dato, self.cabeza)
        self.cabeza = auxinsertar
        print("Elemento insertado")

    def modificar(self, datoantiguo, datonuevo):
        if self.cabeza:
            auxnodo = self.cabeza
            while auxnodo != None:
                if auxnodo.dato == datoantiguo:
                    auxnodo.dato = datonuevo
                    print("Valor modificado con exito.")
                    return
                auxnodo = auxnodo.siguiente
            print("El valor que quiso modificar no existe en la lista.")
            return
        else:
            print("La lista esta vacia.")
            return
    
    def listar(self):
        if self.cabeza:
            auxnodo = self.cabeza
            while auxnodo != None:
                print("Valor: " + auxnodo.dato)
                auxnodo = auxnodo.siguiente
        else:
            print("La lista esta vacia.")
    
    def eliminar(self, dato):
        if self.cabeza:
            auxnodo = self.cabeza
            nodoanterior = self.cabeza
            while auxnodo != None:
                if(auxnodo.dato == dato):
                    if nodoanterior == auxnodo:
                        self.cabeza = auxnodo.siguiente
                    else:
                        nodoanterior.siguiente = auxnodo.siguiente
                    print("El valor se elimino.")
                    return
                nodoanterior = auxnodo
                auxnodo = auxnodo.siguiente
            print("El valor no existe en la lista.")
        else:
            print("La lista esta vacia.")

    def menu(self):
        opcion = 0
        while True:
            opcion = int(input("Introduzca la opcion que desea realizar.\n1. Insertar\n2. Modificar\n3. Listar\n4. Eliminar\n"))
            if(opcion == 5):
                break
            else:
                if opcion == 1:
                    valor = input("Introduzca lo que desea guardar: \n")
                    self.insertar(valor)
                else:
                    if opcion == 2:
                        valorantiguo = input("Introduzca el valor guardado anteriormente: \n")
                        valornuevo = input("Introduzca el valor con el que sera reemplazado el anterior: \n")
                        self.modificar(valorantiguo, valornuevo)
                    else:
                        if opcion == 3:
                            self.listar()
                        else:
                            valoraeliminar = input("Introduzca el valor que desea eliminar:\n")
                            self.eliminar(valoraeliminar)
lis = lista()
lis.menu()