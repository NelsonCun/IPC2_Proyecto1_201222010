from Matriz import Matriz

class ListaCircular:
    def __init__(self):
        self.primero = None
        self.size = 0
    
    def insertar(self, matriz):
        nuevo = matriz
        if self.primero is None:
            self.primero = nuevo
            nuevo.siguiente = self.primero
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.primero
        self.size += 1
    
    def imprimir(self):
        actual = self.primero
        for i in range(self.size):
            print(actual.nombre)
            actual = actual.siguiente
    
    def buscar(self, nombre):
        actual = self.primero
        while actual.nombre != nombre:
            if actual.siguiente == self.primero:
                return None
            actual = actual.siguiente
        return actual
    
    