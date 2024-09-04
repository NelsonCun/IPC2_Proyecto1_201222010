from xml.dom import minidom
from ListaCircular import ListaCircular
from Matriz import Matriz
from NodoCelda import NodoCelda
from ListaFilas import ListaFilas
from NodoFilas import NodoFilas
from NodoFreq import NodoFreq
def menu():
    print("")
    print("*********************************************")
    print("                 Menú Principal                  ")
    print("1. Cargar archivo")
    print("2. Procesar archivo")
    print("3. Escribir archivo de salida")
    print("4. Mostrar datos del estudiante")
    print("5. Generar gráfica")
    print("6. Salida")
    print("*********************************************")
    print("")
    
    try:
        opc = int(input("La opción que desea realizar es: "))
        if opc < 1 or opc > 6:
            print("\nOpción no válida, por favor intenta de nuevo")
    except ValueError:
        print("\nOpción no válida, por favor intenta de nuevo")
        opc = 0
    
    return opc

def cargar_Archivo():
    # Código para cargar archivo
    rutaArchivo = input("Ingrese la ruta del archivo: ")
    # Lectura del archivo
    doc = minidom.parse(rutaArchivo)
    root = doc.documentElement
    
    #listaMatrices = ListaCircular()
    
    matrices = root.getElementsByTagName('matriz') #Obtenemos todos los nodos matriz
    for matriz in matrices:
        nombreMatriz = matriz.getAttribute('nombre') #Obtenemos el atributo nombre
        filas = int(matriz.getAttribute('n')) #Obtenemos el atributo n
        columnas = int(matriz.getAttribute('m')) #Obtenemos el atributo m
        
        # print(f"\nNombre: {nombreMatriz}, Filas: {filas}, Columnas: {columnas}")
        
        matrizObj = Matriz(nombreMatriz, filas, columnas)
        
        celdas = matriz.getElementsByTagName('dato') #Obtenemos todos los nodos dato
        i = 1
        for celda in celdas:
            fila = int(celda.getAttribute('x'))
            columna = int(celda.getAttribute('y'))
            valor = int(celda.firstChild.data)
            
            # print(f'\n fila: {fila}, columna: {columna}, valor: {valor}')
            celda = NodoCelda(fila, columna, valor)
            print(celda.fila, celda.columna, celda.valor)
            matrizObj.insertar(celda)
            print(f'Se agregó el nodo {i}')
            i += 1
            # Imprimimos la matriz
            
            
        matrizObj.imprimir()
        
        listaMatrices.insertar(matrizObj)
    
    listaMatrices.imprimir()
        
    print("Datos leídos correctamente")
        
def procesarArchivo():
    print("\n Se están creando las matrices de patrones de acceso...")
    actual = listaMatrices.primero
    for matriz in range(listaMatrices.size):
        newMatriz = Matriz(actual.nombre, actual.filas, actual.columnas)
        actual2 = actual.primero
        for i in range(actual.size):
            valor = 0
            if actual2.valor >= 1:
                valor = 1
            newCelda = NodoCelda(actual2.fila, actual2.columna, valor)
            print(f"Se agregó el valor {valor}")
            newMatriz.insertar(newCelda)
            actual2 = actual2.siguiente
        matricesPAcceso.insertar(newMatriz)
        newMatriz.imprimir()
        actual = actual.siguiente
    print("Se crearon las matrices de patrones de acceso correctamente\n")
    
    print("\nCreando matrices reducidas...")
    matrizActual = matricesPAcceso.primero
    for matriz in range(matricesPAcceso.size):
        nuevaMatriz = Matriz(matrizActual.nombre)
        filas = 0
        filasAgregadas = ListaFilas()
        for i in range(matrizActual.filas):
            filaActual = filasAgregadas.primero
            filaAgregada = False
            for fila in range(filasAgregadas.size):
                if filaActual.valor is None:
                    break
                if filaActual.valor == i+1:
                    filaAgregada = True
                    break
                filaActual = filaActual.siguiente
            if filaAgregada == True:
                continue
                
            frecuencia = 0
            agregado = False
            for j in range(i+1,matrizActual.filas):
                iguales = True
                for k in range(matrizActual.columnas):
                    if matrizActual.buscar(i+1,k+1).valor != matrizActual.buscar(j+1,k+1).valor:
                        iguales = False
                        break
                if iguales == True:
                    if frecuencia == 0:
                        for k in range(matrizActual.columnas):
                            nuevoValor = listaMatrices.buscar(matrizActual.nombre).buscar(i+1,k+1).valor + listaMatrices.buscar(matrizActual.nombre).buscar(j+1,k+1).valor
                            nuevoNodo = NodoCelda(nuevaMatriz.filas+1, k+1, nuevoValor)
                            nuevaMatriz.insertar(nuevoNodo)
                        nuevaMatriz.filas = nuevaMatriz.filas+1
                        frecuencia += 1
                    elif frecuencia > 0:
                        for k in range(matrizActual.columnas):
                            nuevoValor = nuevaMatriz.buscar(nuevaMatriz.filas,k+1).valor + listaMatrices.buscar(matrizActual.nombre).buscar(j+1,k+1).valor
                            nuevaMatriz.eliminar(nuevaMatriz.filas,k+1)
                            nuevoNodo = NodoCelda(nuevaMatriz.filas,k+1,nuevoValor)
                            nuevaMatriz.insertar(nuevoNodo)
                        frecuencia += 1                
                    filaNueva = NodoFilas(j+1)
                    filasAgregadas.insertar(filaNueva)
                    agregado = True
            if agregado == False:
                for k in range(matrizActual.columnas):
                    nuevoNodo = NodoCelda(nuevaMatriz.filas+1, k+1, listaMatrices.buscar(matrizActual.nombre).buscar(i+1,k+1).valor)
                    nuevaMatriz.insertar(nuevoNodo)
                filaNueva = NodoFilas(i+1)
                filasAgregadas.insertar(filaNueva)
            NodoFrecuencia = NodoFreq(i+1, frecuencia+1)
            print(f"fila {i+1}, frecuencia {frecuencia+1}")
            print(f"{NodoFrecuencia.fila},{NodoFrecuencia.frecuencia}")
            nuevaMatriz.insertarFreq(NodoFrecuencia)
            filas = filas + 1
                 
        nuevaMatriz.filas = filas
        nuevaMatriz.columnas = matrizActual.columnas
        print(f"Tamaño de matriz reducida: {nuevaMatriz.size}")
        nuevaMatriz.imprimir()
        matricesReducidas.insertar(nuevaMatriz)
        matrizActual = matrizActual.siguiente
                
    print("\nSe crearon las matrices reducidas correctamente\n")


def escribirArchivo():
    doc = minidom.Document()
    root = doc.createElement('matricesReducidas')
    doc.appendChild(root)
    
    actual = matricesReducidas.primero
    for matriz in range(matricesReducidas.size):
        matriz_element = doc.createElement('matriz')
        matriz_element.setAttribute('nombre',actual.nombre + "_Salida")
        matriz_element.setAttribute('n', str(actual.filas))
        matriz_element.setAttribute('m', str(actual.columnas))
        matriz_element.setAttribute('g', str(actual.freqSize))
        
        nodoActual = actual.primero
        for i in range(actual.size):
            print("Entro a esta función")
            nodo_element = doc.createElement('dato')
            nodo_element.setAttribute('x', str(nodoActual.fila))
            nodo_element.setAttribute('y', str(nodoActual.columna))
            nodo_element.appendChild(doc.createTextNode(str(nodoActual.valor)))
            matriz_element.appendChild(nodo_element)
            nodoActual = nodoActual.siguiente
            
        frecuencia = actual.freqPrimero
        for i in range(actual.freqSize):
            nodo_element = doc.createElement('frecuencia')
            nodo_element.setAttribute('g', str(frecuencia.fila))
            nodo_element.appendChild(doc.createTextNode(str(frecuencia.frecuencia)))
            print(f"fila {frecuencia.fila}, frecuencia {frecuencia.frecuencia}")
            matriz_element.appendChild(nodo_element)
            frecuencia = frecuencia.siguiente
            
        root.appendChild(matriz_element)
        actual = actual.siguiente
    
    with open('matricesReducidas.xml', 'w', encoding='UTF-8') as file:
        file.write(doc.toprettyxml(indent='    '))
                   
    print("\n... se está escribiendo archivo de salida")
                    
    
if __name__ == "__main__":
    print("****************** Bienvenido ******************")
    opc = 0
    listaMatrices = ListaCircular()
    matricesPAcceso = ListaCircular()
    matricesReducidas = ListaCircular()
    
    while opc != 6:
        opc = menu()
        
        if opc == 1:
            cargar_Archivo()
        elif opc == 2:
            procesarArchivo()
            
            print("Elemento Ejemplo 3, x=2, y=1, 4")
            nodo = listaMatrices.buscar("Ejemplo").buscar(4,2)
            print(f'fila {nodo.fila}, columna {nodo.columna}, valor {nodo.valor}')
            
            print("Reducida")
            nodo = matricesPAcceso.buscar("Ejemplo").buscar(4,2)
            print(f'fila {nodo.fila}, columna {nodo.columna}, valor {nodo.valor}')
            
        elif opc == 3:
            escribirArchivo()
            print("\n... se está escribiendo archivo de salida")
            
        elif opc == 4:
            print("\nDATOS DEL ESTUDIANTE:")
            print("\nNelson Emanuel Cún Bálan")
            print("Carné: 201222010")
            print("Introducción a la Programación y Computación 2")
            print("Ingeniería en Ciencias y Sistemas")
            print("4to. Semestre")
        elif opc == 5:
            print("\n... se está generando gráfica")
        elif opc == 6:
            print("\n... saliendo...")
    print("*********************************************")
    print("\n Gracias por utilizar nuestro sistema\n")
