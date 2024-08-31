class NodoCelda:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.anterior = None
        self.siguiente = None