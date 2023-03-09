"""Ejercicio 1
Escribir en Python dos funciones que muestran y dos funciones que devuelven.
Ejercicio 2
Escribir en Pyhton funciones que operen sobre un número variable de valores numéricos y devuelvan
los resultados solicitados (una función para cada inciso)
a) Devolver el mínimo de los valores y su posición en la lista de argumentos.
b) Devolver la diferencia entre el menor y el mayor de los argumentos.
c) Devolver el promedio de todos los elementos.
Ejercicio 3
Escribir en Pyhton funciones que operen sobre un número variable de listas y devuelvan los
resultados solicitados (una función para cada inciso)
a) Devolver la lista con menor cantidad de elementos
b) Devolver todas las listas cuya cantidad de elementos sea superior a 5.
c) Devolver todas las listas cuyos elementos sean todos del mismo tipo de dato (considerar sólo
tipos de datos básicos del lenguaje).
d) Devolver todas las listas que contengan al menos 3 elementos de tipo de dato numérico.
Ejercicio 4
Implementar la función analizarDatos, que reciba como parámetros una lista de nombres y una lista
de salarios, ambas con la misma cantidad de elementos y cuya información se relaciona por medio
del mismo índice (concepto de listas paralelas: el dato en la posición i de una lista está relacionado
únicamente con el dato en la misma posición de la otra lista).
La función solicitada debe cumplir los siguientes requisitos:
a) Los dos parámetros deben poder pasarse a la función en cualquier orden.
b) La función debe devolver un diccionario, con las siguientes claves: “error”, “mayor”, “menor”,
“promedio”.
c) Si las longitudes de las listas no coinciden, la función debe devolver un mensaje apropiado como
valor en la clave “error”. Todas las demás claves deben tomar valor None.
d) Se debe controlar que todos los valores de la lista de salarios sean positivos, de lo contrario
indicar un mensaje apropiado como valor en la clave “error”. Todas las demás claves deben tomar
valor None.
e) Se debe controlar que todos los valores de la lista de nombres sean cadenas no vacías, de lo
contrario indicar un mensaje apropiado como valor en la clave “error”. Todas las demás claves deben
tomar valor None.
f) Si todos los datos de entrada son correctos, devolver en las claves correspondientes los datos de:
nombre y salario de la persona con menor salario, nombre y salario de la persona con mayor salario,
promedio de todos los salarios."""

def Punto1a(paramRecibido):

    print(paramRecibido)
def Punto1b():
    parametro = ""
    return parametro

def Punto2a(numeros):

    min = min(numeros)
    indice = numeros.index(min)
    return min, indice

def Punto2b(numeros):
    min = min(numeros)
    max = max(numeros)

    diferencia = max - min

    return diferencia

def Punto2c(numeros):
    sumaTotal = 0
    cantNumeros = len(numeros)

    for i in numeros:
        sumaTotal = sumaTotal + i

    promedio = sumaTotal / cantNumeros

    return promedio

def Punto3a(*listas):
    """a) Devolver la lista con menor cantidad de elementos
b) Devolver todas las listas cuya cantidad de elementos sea superior a 5.
c) Devolver todas las listas cuyos elementos sean todos del mismo tipo de dato (considerar sólo
tipos de datos básicos del lenguaje).
d) Devolver todas las listas que contengan al menos 3 elementos de tipo de dato numérico."""
    longitud = []

    for i in listas:
        var = len(i)        #Variable para ir guardando la cantidad de elementos de cada lista
        longitud.append(var)    #appendizo la cantidad de deleemntos de cada lista en la lista longitud
    menor = min(longitud)               #Busco el menor valor en las longitudes que voy guardando
    indiceMenor = longitud.index(menor) #Busco el indice de la lista con menor longitud, que va a ser el mismo indice de la lista de listas

    return(listas[indiceMenor]) #retorno la lista de listas con la lista de menor elementos que guarde anteriormente


def Punto3b(*listas):

    longitud = []

    for i in listas:
        var = len(i)        #Variable para saber la longitud de la lista

        if var > 5:         #Si tiene mas de 5 elemntos, guardo la lista en la lista variable longitud
            longitud.append(i)
    return(longitud)

def Punto3c(*listas):
    """c) Devolver todas las listas cuyos elementos sean todos del mismo tipo de dato (considerar sólo
tipos de datos básicos del lenguaje)."""
    datoTipo = []
    iguales = True
    cantListas= len(listas)
    liSeparadas = []
    var = 0


    for i in listas:                #FALTA HACER

        liSeparadas.append(i)
        var = len(i)
        for x in i:
            tipo = type(x)              #RECORRO LAS LISTAS Y VEO EL TIPO DE DATO DE CADA ELEMENTO DE LA LISTA
            datoTipo.append(tipo)

            for j in datoTipo[:var]:
                if j != datoTipo[0]:
                    iguales = False

    return (datoTipo, liSeparadas, iguales)






lista1=[1,2,3]
lista2=[4,5,6,7]
lista3=[8,9]
lista4=[1,1,1,1,1,1]
lista5=[2,3,3,4,5,5,5]
multilistas = [[1,2,3], [4,5,6], [0,9,8], [1,5,2]]
#print(Punto3c(lista1, lista2, lista3))


def Punto4a(liNom, liSal):
    """Ejercicio 4
Implementar la función analizarDatos, que reciba como parámetros una lista de nombres y una lista
de salarios, ambas con la misma cantidad de elementos y cuya información se relaciona por medio
del mismo índice (concepto de listas paralelas: el dato en la posición i de una lista está relacionado
únicamente con el dato en la misma posición de la otra lista).
La función solicitada debe cumplir los siguientes requisitos:
a) Los dos parámetros deben poder pasarse a la función en cualquier orden.
b) La función debe devolver un diccionario, con las siguientes claves: “error”, “mayor”, “menor”,
“promedio”.
c) Si las longitudes de las listas no coinciden, la función debe devolver un mensaje apropiado como
valor en la clave “error”. Todas las demás claves deben tomar valor None.
d) Se debe controlar que todos los valores de la lista de salarios sean positivos, de lo contrario
indicar un mensaje apropiado como valor en la clave “error”. Todas las demás claves deben tomar
valor None.
e) Se debe controlar que todos los valores de la lista de nombres sean cadenas no vacías, de lo
contrario indicar un mensaje apropiado como valor en la clave “error”. Todas las demás claves deben
tomar valor None.
f) Si todos los datos de entrada son correctos, devolver en las claves correspondientes los datos de:
nombre y salario de la persona con menor salario, nombre y salario de la persona con mayor salario,
promedio de todos los salarios."""

    relacion = list(zip(liNom, liSal))
    diccionario = {"Error": None, "mayor": None, "menor": None, "pomedio": None}

    if len(liNom) != len(liSal):
        return diccionario["error"]

    for i in liSal:
        if i < 0:
            return diccionario["error"]

    for i in liNom:
        if i == " ":
            return diccionario["error"]






    return relacion

#listaN=["juan perez", "marta rodriguez"]
#listaS=[1400.20 , 1050.50]
#print(Punto4a(listaN, listaS))


def primerFiltro(lista1, lista2):
    cumple = len(lista1) == len(lista2)
    return cumple

def segundoFiltro(listaSalarios):
    cumple = True
    for i in listaSalarios:
        if i <= 0 :
            cumple = False
            break
    return cumple
    """    indice = 0
    while (cumple == True) and (indice < len(listaSalarios)):
        unSalario = listaSalarios[indice]
        indice+=1
        if unSalario<0:
            cumple = False"""

def tercerFiltro(listaNombres):
    cumple = True
    for i in listaNombres:
        if len(listaNombres)<3 :                  # or len(listaNombres) == 0 es lo mismo
            cumple = False
            break
    return cumple

    return cumple

def cumpleTodo(listaNombres, listaSueldos):

    #obtenemos al menor sueldo y su nombnre correspondiente
    menor = min(listaSueldos)
    posicionMin = listaSueldos.index(menor)
    nombreMenor = listaNombres[posicionMin]     #aca obtengo al menor

    #obtenemos al mayor sueldo
    mayor = max(listaSueldos)
    posicionMax = listaSueldos.index(mayor)
    nombreMayor = listaNombres[posicionMax]     #aca obtengo al nombre del mayor salario

    #calcular promedio
    promedio = sum(listaSueldos)/len(listaSueldos)  #aca obtengo el promedio

    return menor, nombreMenor, mayor, nombreMayor, promedio

def analizarDatos(listaNombres = [], listaSueldos = []):
    #vamos a hacer filtros
    diccionario = {"Error": None,
                   "mayor": None,
                   "menor": None,
                   "pomedio": None}

    #si cumplimos los 3 , calcular mayor salario, menor salario y el promedio de los salarios#

    cumple1 = primerFiltro(listaNombres, listaSueldos)
    cumple2 = segundoFiltro(listaSueldos)
    cumple3 = tercerFiltro(listaNombres)

    if cumple1 == False:
        diccionario.update({"Error": "Las listas son desiguales"})         #actualizo el diccionario
    elif cumple2 == False:
        diccionario.update({"Error": "Hay salario/s negativos"})
    elif cumple3 == False:
        diccionario.update({"Error": "Hay nombres con cadenas vacias"})
    else:
        cumpleTodo(listaNombres, listaSueldos)

    if cumple1 and cumple2 and cumple3:
        menor, nombreMenor, mayor, nombreMayor, promedio = cumpleTodo(listaNombres,listaSueldos)
        diccionario.update({"mayor": f"el mayor salario es de {nombreMayor} y es de {mayor}",
                            "menor": f"el mayor salario es de {nombreMenor} y es de {menor}",
                            "pomedio": f"el promedio de salarios es {promedio}"})

    return diccionario
