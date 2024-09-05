from NodoCelda import NodoCelda
from NodoFreq import NodoFreq
import os
from os import system
def startfile(filepath):
    os.system(f'open "{filepath}"')

class Matriz:
    def __init__(self, nombre, filas=0, columnas=0):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.size = 0
        self.primero = None
        self.ultimo = None
        self.siguiente = None
        self.freqPrimero = None
        self.freqUltimo = None
        self.freqSize = 0
        self.freqSiguiente = None
        
    def insertar(self, celda):
        nuevo = celda
        
        # Caso 1: La lista está vacía
        if self.primero is None:
            self.primero = nuevo
            self.ultimo = nuevo
            self.size += 1
            #print(f"Se agregó el nodo {nuevo.fila, nuevo.columna, nuevo.valor} como el primero")
            return
        
        actual = self.primero
        
        # Caso 2: Insertar al principio (antes del primer nodo)
        if nuevo.fila < actual.fila or (nuevo.fila == actual.fila and nuevo.columna < actual.columna):
            nuevo.siguiente = actual
            actual.anterior = nuevo
            self.primero = nuevo
            self.size += 1
            #print(f"Se agregó el nodo {nuevo.fila, nuevo.columna, nuevo.valor} al principio")
            return
        
        # Caso 3: Insertar en el medio o al final
        while actual is not None:
            if (nuevo.fila < actual.fila) or (nuevo.fila == actual.fila and nuevo.columna < actual.columna):
                nuevo.siguiente = actual
                nuevo.anterior = actual.anterior
                if actual.anterior is not None:
                    actual.anterior.siguiente = nuevo
                actual.anterior = nuevo
                self.size += 1
                #print(f"Se agregó el nodo {nuevo.fila, nuevo.columna, nuevo.valor} en el medio")
                return
            
            if actual.siguiente is None:
                # Caso 4: Insertar al final
                actual.siguiente = nuevo
                nuevo.anterior = actual
                self.ultimo = nuevo
                self.size += 1
                #print(f"Se agregó el nodo {nuevo.fila, nuevo.columna, nuevo.valor} al final")
                return
            
            actual = actual.siguiente
                
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
    
    def eliminar(self, fila, columna):
        actual = self.primero
        while actual != None:
            if actual.fila == fila and actual.columna == columna:
                if actual.anterior != None:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.primero = actual.siguiente
                if actual.siguiente != None:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.ultimo = actual.anterior
                self.size -= 1
                break
            actual = actual.siguiente
            
    def insertarFreq(self, nodoFreq):
        nuevo = nodoFreq
        if self.freqPrimero == None:
            self.freqPrimero = nuevo
            self.freqSize += 1
            #print(f"Se agregó la frecuencia para fila: {nuevo.fila} frecuencia: {nuevo.frecuencia} opcion 0")
        else:
            #print("Se entró a la opción extra")
            actual = self.freqPrimero
            for i in range(self.freqSize):
                if actual.siguiente == None:
                    actual.siguiente = nuevo
                actual = actual.siguiente
            self.freqSize += 1
            #print(f"Se agregó la frecuencia para fila: {nuevo.fila} frecuencia: {nuevo.frecuencia} opcion 1")
                
    def buscarFreq(self, fila):
        actual = self.freqPrimero
        while actual != None:
            if actual.fila == fila:
                return actual.frecuencia
            actual = actual.siguiente
        return None
    
    def crearGraphviz(self):
        print("\n... se está generando gráfica de la matriz original")
        if self.filas == 0 or self.columnas == 0:
            print("Dimensiones inválidas")
            return
        
        # Crear el texto DOT
        textoDOT = f'''digraph G {{ \n
            rankdir=TB; \n
            node[shape=plaintext]; \n
            edge[style=bold]; \n
            
            inicio [label="Matrices" shape=oval style=bold]; \n
            header [label="{self.nombre}" shape=oval style=bold]; \n
            
            subgraph cluster_side {{\n
            node [shape=plaintext]; \n
                filas [label="m = {self.filas}" shape=oval style=bold]; \n
                columnas [label="n = {self.columnas}" shape=oval style=bold]; \n
                }}
            
            matriz [\n
            label=<<TABLE border="1" cellspacing="0" cellpadding="10">\n
            '''
        
        # Añadir filas y columnas
        actual = self.primero
        for i in range(self.filas):
            textoDOT += "   <tr>\n"
            for j in range(self.columnas):
                textoDOT += f"<td>{str(actual.valor)}</td>\n"
                actual = actual.siguiente
            textoDOT += "   </tr>\n"

        textoDOT += ''' </TABLE>\n
            >];
            
            // Conectar los nodos
            inicio -> header;
            header -> filas;
            header -> columnas;
            header -> matriz;
        }
        '''

        # Escribir el archivo DOT
        nombreSalida = self.nombre + ".dot"
        with open(nombreSalida, "w") as dot_file:
            dot_file.write(textoDOT)

        # Ejecutar Graphviz para generar el PDF
        system('dot -Tpdf ' + nombreSalida + ' -o ' + self.nombre + ".pdf ")
        startfile(self.nombre + ".pdf ")
        
    def crearGraphviz2(self):
        print("\n... se está generando gráfica de la matriz reducida...")
        if self.filas == 0 or self.columnas == 0:
            print("Dimensiones inválidas")
            return
        
        # Crear el texto DOT
        textoDOT = f'''digraph G {{ \n
            rankdir=TB; \n
            node[shape=plaintext]; \n
            edge[style=bold]; \n
            
            inicio [label="Matrices Reducidas" shape=oval style=bold]; \n
            header [label="{self.nombre}_Salida" shape=oval style=bold]; \n
            
            subgraph cluster_side {{\n
            node [shape=plaintext]; \n
                filas [label="m = {self.filas}" shape=oval style=bold]; \n
                columnas [label="n = {self.columnas}" shape=oval style=bold]; \n
                }}
            
            matriz [\n
            label=<<TABLE border="1" cellspacing="0" cellpadding="10">\n
            '''
        
        # Añadir filas y columnas
        actual = self.primero
        for i in range(self.filas):
            textoDOT += "   <tr>\n"
            for j in range(self.columnas):
                textoDOT += f"<td>{str(actual.valor)}</td>\n"
                actual = actual.siguiente
            textoDOT += "   </tr>\n"

        textoDOT += ''' </TABLE>\n
            >];
            
            // Conectar los nodos
            inicio -> header;
            header -> filas;
            header -> columnas;
            header -> matriz;
        }
        '''

        # Escribir el archivo DOT
        nombreSalida = self.nombre + "_Salida.dot"
        with open(nombreSalida, "w") as dot_file:
            dot_file.write(textoDOT)

        # Ejecutar Graphviz para generar el PDF
        system('dot -Tpdf ' + nombreSalida + ' -o ' + self.nombre + "_Salida.pdf ")
        startfile(self.nombre + ".pdf ")