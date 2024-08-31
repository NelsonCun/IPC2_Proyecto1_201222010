from xml.dom import minidom
from ListaCircular import ListaCircular
from Matriz import Matriz
from NodoCelda import NodoCelda
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
        
    
    
if __name__ == "__main__":
    print("****************** Bienvenido ******************")
    opc = 0
    listaMatrices = ListaCircular()
    while opc != 6:
        opc = menu()
        
        if opc == 1:
            cargar_Archivo()
        elif opc == 2:
            print("Elemento Ejemplo 3, x=2, y=1, 4")
            nodo = listaMatrices.buscar("Ejemplo3").buscar(2,1)
            print(f'fila {nodo.fila}, columna {nodo.columna}, valor {nodo.valor}')
            
        elif opc == 3:
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
