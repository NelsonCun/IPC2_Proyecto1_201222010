class ListaFilas:
    def __init__(self):
        self.primero = None
        self.size = 0
        
    def insertar(self, fila):
        nuevo = fila
        if self.primero is None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.size += 1