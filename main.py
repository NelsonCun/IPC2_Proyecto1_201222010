class Main:
    x = 0
    print("****************** Bienvenido ******************")
    
    while x != 6:
        print("")
        print("*********************************************")
        print("                 Menú Principal                  ")
        print("1. Cargar archivo")
        print("2. Procesar archivo")
        print("3. Escribir archivo de salida")
        print("4. Mostrar datos del estudiante")
        print("5. Generar gráfica")
        print("6. Salida")
       
       # Validación de la opción ingresada
        try:
            x = int(input("La opción que desea realizar es: "))
            if x < 1 or x > 6:
                print("\nOpción no válida, por favor intenta de nuevo")
        except ValueError:
            print("\nOpción no válida, por favor intenta de nuevo")
        
        if x == 1:
            print("\n... se está cargando archivo")
        elif x == 2:
            print("\n... se está procesando archivo")
        elif x == 3:
            print("\n... se está escribiendo archivo de salida")
        elif x == 4:
            print("\nDATOS DEL ESTUDIANTE:")
            print("\nNelson Emanuel Cún Bálan")
            print("Carné: 201222010")
            print("Introducción a la Programación y Computación 2")
            print("Ingeniería en Ciencias y Sistemas")
            print("4to. Semestre")
        elif x == 5:
            print("\n... se está generando gráfica")
        elif x == 6:
            print("\n... saliendo...")
    print("*********************************************")
    print("\n Gracias por utilizar nuestro sistema\n")
