def escribirArchivoMD():
    doc = minidom.Document() #Crear un documento
    root = doc.createElement('listadoResporte') #Crear un elemento raíz
    doc.appendChild(root) #Agregar el elemento raíz al documento
    
    for banco in listaBancos: #Iterar sobre los bancos
        banco_element = doc.createElement('Banco') #Crear un elemento Banco
        banco_element.setAttribute('nombre', banco.nombre)
        
        direccion_element = doc.createElement('direccion') #Crear un elemento dirección
        direccion_element.appendChild(doc.createTextNode(banco.direccion)) #Agregar el texto de la dirección
        banco_element.appendChild(direccion_element) #Agregar el elemento dirección al elemento banco
        
        promedio_element = doc.createElement('promedio') #Crear un elemento promedio
        promedio_element.appendChild(doc.createTextNode(str(banco.promedio()))) #Agregar el texto del promedio
        banco_element.appendChild(promedio_element) #Agregar el elemento promedio al elemento banco
        
        root.appendChild(banco_element) #Agregar el elemento banco al elemento raíz
    
    with open('promedioPorBanco_MD.xml', 'w', encoding='UTF-8') as file: #Abrir el archivo en modo escritura
        file.write(doc.toprettyxml(indent='    ')) #Escribir el archivo XML