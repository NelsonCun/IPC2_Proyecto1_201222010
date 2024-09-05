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
    
    def eliminar(self, nombre):
        if self.primero is None:  # Caso: lista vacía
            return
        
        actual = self.primero
        previo = None
        
        # Caso especial: si la lista tiene un solo elemento
        if self.size == 1 and actual.nombre == nombre:
            self.primero = None
            self.size = 0
            return
        
        # Caso: eliminar el primer nodo
        if actual.nombre == nombre:
            # Encontrar el último nodo para mantener la circularidad
            ultimo = self.primero
            while ultimo.siguiente != self.primero:
                ultimo = ultimo.siguiente
            
            # Actualizar el primero y el siguiente del último
            self.primero = actual.siguiente
            ultimo.siguiente = self.primero
            self.size -= 1
            return
        
        # Caso: eliminar un nodo que no es el primero
        while actual.siguiente != self.primero and actual.nombre != nombre:
            previo = actual
            actual = actual.siguiente
        
        if actual.nombre == nombre:
            previo.siguiente = actual.siguiente
            self.size -= 1