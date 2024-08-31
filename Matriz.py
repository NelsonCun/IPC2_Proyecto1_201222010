from NodoCelda import NodoCelda

class Matriz:
    def __init__(self, nombre, filas, columnas):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.size = 0
        self.primero = None
        self.ultimo = None
        self.siguiente = None
        
    def insertar(self, celda):
        nuevo = celda
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
            self.size += 1
            print(f"Se agregó el nodo {nuevo.fila, nuevo.columna, nuevo.valor} opcion 0")
        else:
            print("Se entró a la opción extra")
            actual = self.ultimo
            for i in range(self.size):
                print('Se entró aquí {i} veces')
                if nuevo.fila > actual.fila or (nuevo.fila == actual.fila and(nuevo.columna > actual.columna)):
                    actual.siguiente = nuevo
                    nuevo.anterior = actual
                    self.ultimo = nuevo
                    print(f"Se agregó el nodo {nuevo.fila, nuevo.columna, nuevo.valor} opcion 1")
                    self.size += 1
                    break
                elif (nuevo.fila < actual.fila and (nuevo.fila > actual.anterior.fila or actual.anterior == None)) or (nuevo.fila == actual.fila and (nuevo.columna < actual.columna and (nuevo.columna > actual.anterior.columna or actual.anterior == None))):
                    nuevo.siguiente = actual
                    nuevo.anterior = actual.anterior
                    if actual.anterior!= None:
                        actual.anterior.siguiente = nuevo
                    else:
                        self.primero = nuevo
                    actual.anterior = nuevo
                    print(f"Se agregó el nodo {nuevo.fila, nuevo.columna, nuevo.valor} opcion 2")
                    self.size += 1
                    break
                actual = actual.anterior
                
    def imprimir(self):
        actual = self.primero
        for i in range(self.size):
            print(f" x={actual.fila}, y={actual.columna}, valor={actual.valor}")
            actual = actual.siguiente
            
    def buscar(self, fila, columna):
        actual = self.primero
        for i in range(self.size):
            if actual.fila == fila and actual.columna == columna:
                return actual
            actual = actual.siguiente
        return None