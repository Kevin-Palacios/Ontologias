import pathlib
import os
import pandas as pd


def ingresarDatos(ruta, tipo, archivo, n, acceso):
    lista = []
    if tipo == "c":
        palabra = "caracteristica"
    else:
        palabra = "elemento"
    
    with open(ruta+tipo+archivo, acceso) as archivoc:
        for i in range(n):
            print(f"Ingresa la {palabra} numero {i+1}")
            caracteristica = input()
            lista.append(caracteristica)
            archivoc.write(caracteristica+"\n")

    return lista


def enlistarCaracteristicas(ruta, caracteristicas, elementos):
    i, j= 0, 0
    matriz = []
    with open(ruta, "w") as archivo:
        for elemento in elementos:
            j=0
            matriz.append([])
            for caracteristica in caracteristicas:
                print(f"Ingresa el valor de {caracteristica} en {elemento}:")
                valor = input()
                if j == len(caracteristicas)-1:
                    archivo.write(valor+"\n")
                else:
                    archivo.write(valor+",")
                matriz[i].append(valor)
                j+=1
            i+=1

    return matriz

def seleccionar(dir, tipo, valor):
    
    i = 0
    valores = []
    with open(dir+tipo+valor) as archivo:
        for linea in archivo:
            elemento = linea.replace("\n", "")
            valores.append(elemento)
            i += 1
            print(f"{i}. {elemento}")
    indice = int(input()) - 1
    while indice < 0 or indice > i-1:
        print("Valor invalido, ingresa uno válido")
        indice = int(input()) - 1
    valor = valores[indice]
    print(valor)

    return valores, indice

def obtenerListaTxt(dir, tipo, nombreArchivo):
    lista = []
    with open(dir+tipo+nombreArchivo, 'r') as archivo:
        lista = archivo.readlines()
    lista = [linea.rstrip('\n') for linea in lista]
    return lista

def buscarEnArchivo(dir, tipo, nombreArchivo, palabra):
    numLienea = -1
    contador = 0
    with open(dir+tipo+nombreArchivo) as archivo:
        for linea in archivo:
            if palabra == linea.replace("\n", ""):
                return [True, contador]
            contador += 1

    return [False, numLienea]

def agregarArchivo(dir, tipo, nombreArchivo, palabra):

    with open(dir+tipo+nombreArchivo, "a") as archivo:
        archivo.write(palabra+"\n")

def editarArchivo(dir, tipo, nombreArchivo, nueva_linea, linea_a_reemplazar, borrar=False):
    archivo_original = dir+tipo+nombreArchivo
    # Archivo temporal para almacenar los cambios
    archivo_temporal = dir+tipo+'temporal.txt'
    with open(archivo_original, 'r') as archivo_lectura, open(archivo_temporal, 'w') as archivo_temp:
        for indice, linea in enumerate(archivo_lectura, 1):
            if indice == linea_a_reemplazar:
                if borrar:
                    continue
                archivo_temp.write(nueva_linea+"\n")
            else:
                archivo_temp.write(linea)

    # Renombrar el archivo temporal para que reemplace al original
    os.replace(archivo_temporal, archivo_original)
    pass

matriz = [[]]
caracteristicas=[]
elementos = []
dir = "Ontologia/ontologias/"
opcion = 1
while(opcion>=1 and opcion<=3):
    print("Elige una opcion:")
    print("1. Crear ontología")
    print("2. Seleccionar ontología")
    print("3. Borrar ontología")
    print("4. Salir")

    opcion = int(input())

    if opcion == 1:
        print("Se crea ontologia")

        print("Ingresa el nombre de la ontologia")
        nombre = input()
        archivo = nombre+".txt"
        print(dir+archivo)
        if os.path.isfile(dir+archivo):
            print("Esa ruta ya existe")
            continue

        with open("Ontologia/ontologias.txt", "a") as aonto:
            aonto.write(nombre+"\n")

        print("Ingresa el numero de caracteristicas")
        n_caracteristicas = int(input())
        caracteristicas = ingresarDatos(dir, "c", archivo, n_caracteristicas, "w")
        

        print("Ingresa el numero de elementos")
        n_elementos = int(input())
        elementos = ingresarDatos(dir, "e", archivo, n_elementos, "w")

        matriz = enlistarCaracteristicas(dir+archivo, caracteristicas, elementos)

        print(matriz)
        

    elif opcion == 2:

        listaOntologias = []
        i = 0
        with open("Ontologia/ontologias.txt") as archivo:
            for linea in archivo:
                #if linea != "":
                    valor = linea.replace("\n", "")
                    listaOntologias.append(valor+".txt")
                    if len(listaOntologias) == 1:
                        print("Selecciona alguna ontología")

                    i += 1
                    print(f"{i}. {valor}")

        
        if i == 0:
            print("No se encontraron ontologías")
            continue
        indice = int(input()) - 1
        while indice < 0 or indice > len(listaOntologias)-1:
            print("Valor invalido, ingresa uno válido")
            indice = int(input()) - 1

        valor = listaOntologias[indice]
        
        opcion2 = 0
        
        print("Elige una opcion:")
        print("1. Clasificar por caracteristica")
        print("2. Agregar caracteristica")
        print("3. Agregar elemento")
        print("4. Eliminar caracteristica")
        print("5. Eliminar elemento")
        print("6. Editar caracteristica")
        print("7. Editar elemento")
        print("8. Editar valor")
        print("9. Salir")

        opcion2 = int(input())
        print(opcion2)

        if opcion2 == 1:
            print("Selecciona alguna caracteristica")
            valoresC, indiceC = seleccionar(dir, "c", valor)
            """
            i = 0
            valoresC = []
            with open(dir+"c"+valor) as archivo:
                for linea in archivo:
                    caracteristica = linea.replace("\n", "")
                    valoresC.append(caracteristica)
                    i += 1
                    print(f"{i}. {caracteristica}")
            indiceC = int(input()) - 1
            while indiceC < 0 or indiceC > i-1:
                print("Valor invalido, ingresa uno válido")
                indiceC = int(input()) - 1
            valorCaracteristica = valoresC[indiceC]
            print(valorCaracteristica)
            """

            print("Selecciona algun elemento")
            valoresE, indiceE = seleccionar(dir, "e", valor)
            """
            i = 0
            valoresE = []
            with open(dir+"e"+valor) as archivo:
                for linea in archivo:
                    elemento = linea.replace("\n", "")
                    valoresE.append(elemento)
                    i += 1
                    print(f"{i}. {elemento}")
            indiceE = int(input()) - 1
            while indiceE < 0 or indiceE > i-1:
                print("Valor invalido, ingresa uno válido")
                indiceE = int(input()) - 1
            valorElemento = valoresE[indiceE]
            print(valorElemento)
            """

            dataframe = pd.read_csv(dir+valor, delimiter=",", header=None)
            print(dataframe[indiceC][indiceE])
            print(dataframe[indiceC])
            print(dataframe.shape[0])
            comparacion = dataframe[indiceC][indiceE]
            similitudes = []
            for i in range(dataframe.shape[0]):
                if i != indiceE:
                    similitudes.append({"Elemento":valoresE[i], "Cercania":abs(comparacion-dataframe[indiceC][i])})
            
            print(similitudes)
            similitudesOrdenadas = sorted(similitudes, key=lambda x: x['Cercania'])
            print("Similitudes ordenadas:")
            print(similitudesOrdenadas)


        elif opcion2 == 2:

            listaC = obtenerListaTxt(dir, "c", valor)
            print(f"Ingresa el nombre de la nueva caracteristica")
            nuevaCaracteristica = input()
            if nuevaCaracteristica in listaC:
                print("Ese elemento ya existe")
                continue
            
            agregarArchivo(dir,"c", valor, nuevaCaracteristica)
            
            
            lineas = []
            with open(dir+valor) as archivo:
                lineas = archivo.readlines()

            listaE = obtenerListaTxt(dir, "e", valor)
            #print(listaC)
            contador = 0
            nuevosValores = []
            for e, linea in zip(listaE, lineas):
                linea = linea.replace("\n", "")
                linea = linea.split(",")
                nuevosValores = linea
                print(f"Ingresa el valor de {nuevaCaracteristica} en {e}")
                nuevoVal = input()
                nuevosValores.append(nuevoVal)
                contador+=1
                editarArchivo(dir,"", valor, ",".join(nuevosValores), contador)


        elif opcion2 == 3:
            print("Ingresa el elemento a agregar")
            nuevoElemento = input()
            if buscarEnArchivo(dir, "e", valor, nuevoElemento):
                print("Ya existe ese elemento")
                continue
            
            agregarArchivo(dir, "e", valor, nuevoElemento)

            nuevosValores = ""

            with open(dir+"c"+valor) as archivo:
                for linea in archivo:
                    caracteristica = linea.replace("\n", "")
                    print(f"Ingresa el valor de {nuevoElemento} en {caracteristica}")
                    nuevosValores = nuevosValores + input() + ","
            agregarArchivo(dir, "", valor, nuevosValores[:-1])


        elif opcion2 == 4:
            print("Selecciona la caracteristica a eliminar")
            _, indiceC = seleccionar(dir, "c", valor)

            editarArchivo(dir,"c", valor, "", indiceC+1, borrar=True)

            lineas = []
            with open(dir+valor) as archivo:
                lineas = archivo.readlines()
                
            #print(listaC)
            contador = 0
            nuevosValores = []
            for linea in lineas:
                linea = linea.replace("\n", "")
                linea = linea.split(",")
                nuevosValores = linea
                
                del nuevosValores[indiceC]
                contador+=1
                editarArchivo(dir,"", valor, ",".join(nuevosValores), contador)
        elif opcion2 == 5:
            print("Selecciona el elemento a eliminar")
            _, indiceE = seleccionar(dir, "e", valor)

            editarArchivo(dir,"e", valor, "", indiceE+1, borrar=True)

            editarArchivo(dir,"", valor, "", indiceE+1, borrar=True)

        elif opcion2 == 6:
            print("Selecciona la caracteristica a modificar")
            valoresC, indiceC = seleccionar(dir, "c", valor)
            print(f"Con que nueva caracteristica quieres reemplazar {valoresC[indiceC]}")
            nuevaCaracteristica = input()
            if nuevaCaracteristica in valoresC:
                print("Ese elemento ya existe")
            else:
                editarArchivo(dir,"c", valor, nuevaCaracteristica, indiceC+1)

            print("Quieres modificar los valores de los elementos?")
            print("1. Si")
            print("2. No")
            modificar = int(input())
            if modificar != 1:
                continue
            valores = []
            with open(dir+valor) as archivo:
                for linea in archivo:                    
                    linea = linea.replace("\n", "")
                    linea = linea.split(",")
                    valores.append(linea[indiceC])
            lineas = []
            with open(dir+valor) as archivo:
                lineas = archivo.readlines()

            print("Indice: ", indiceC)
            print("Valores: ", valores)
            
            listaE = obtenerListaTxt(dir, "e", valor)
            #print(listaC)
            contador = 0
            nuevosValores = []
            for e, v, linea in zip(listaE, valores, lineas):
                linea = linea.replace("\n", "")
                linea = linea.split(",")
                nuevosValores = linea
                print(f"Ingresa el valor de {nuevaCaracteristica} en {e}, el anterior era {v}")
                print("Si no quieres modificar ese valor deja en blanco")
                nuevoVal = input()
                if nuevoVal == "":
                    nuevosValores[indiceC] = v
                else:
                    nuevosValores[indiceC] = nuevoVal
                contador+=1
                editarArchivo(dir,"", valor, ",".join(nuevosValores), contador)
            
        elif opcion2 == 7:
            print("Selecciona el elemento a modificar")
            valoresE, indiceE = seleccionar(dir, "e", valor)
            print(f"Con que nuevo elemento quieres reemplazar {valoresE[indiceE]}")
            nuevoElemento = input()
            if nuevoElemento in valoresE:
                print("Ese elemento ya existe")
            else:
                editarArchivo(dir,"e", valor, nuevoElemento, indiceE+1)

            print("Quieres modificar los valores de sus caracteristicas?")
            print("1. Si")
            print("2. No")
            modificar = int(input())
            if modificar != 1:
                continue
            valores = []
            with open(dir+valor) as archivo:
                for i in range(indiceE+1):
                    linea = archivo.readline()
                    #print("I: ", i)
                    #print("Linea: ", linea)
                    if i == indiceE:
                        linea = linea.replace("\n", "")
                        valores = linea.split(",")
                        break
            #print("Indice: ", indiceE)
            #print("Valores: ", valores)
            listaC = obtenerListaTxt(dir, "c", valor)
            #print(listaC)
            nuevosValores = ""
            for c, v in zip(listaC, valores):
                print(f"Ingresa el valor de {c} en {nuevoElemento}, el anterior era {v}")
                print("Si no quieres modificar ese valor deja en blanco")
                nuevoVal = input()
                if nuevoVal == "":
                    nuevosValores = nuevosValores + v + ","
                else:
                    nuevosValores = nuevosValores + nuevoVal + ","
            
            editarArchivo(dir,"", valor, nuevosValores[:-1], indiceE+1)
            
        elif opcion2 == 8:
            print("Selecciona el elemento a modificar")
            listaE, indiceE = seleccionar(dir, "e", valor)

            print("Selecciona la caracteristica a modificar")
            listaC, indiceC = seleccionar(dir, "c", valor)

            valores = []
            with open(dir+valor) as archivo:
                for i in range(indiceE+1):
                    linea = archivo.readline()
                    #print("I: ", i)
                    #print("Linea: ", linea)
                    if i == indiceE:
                        linea = linea.replace("\n", "")
                        valores = linea.split(",")
                        break
                    
            #print(listaC)
            print(f"Ingresa el valor de {listaC[indiceC]} en {listaE[indiceE]}, el anterior era {valores[indiceC]}")
            print("Si no quieres modificar ese valor deja en blanco")
            nuevoVal = input()
            if nuevoVal != "":
                valores[indiceC] = nuevoVal
        
            editarArchivo(dir,"", valor,  ",".join(valores), indiceE+1)
            
        
        




