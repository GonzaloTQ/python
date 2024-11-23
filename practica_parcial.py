from queue import Queue as Cola


# Ejercicio 1
#
#  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#    requiere: {e pertenece a s }
#    asegura: {res es la posición de la última aparición de e en s}
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,100,0,100,0,-1,-1]
#   e = 0
# se debería devolver res=7

#recorro la lista de atras para adelante para asegurarme de que la aparicion del elemento que busco sea la ultima en la lista

def ultima_aparcion (s:list, e:int) -> int:
    indice:int = 0
    longitud = len(s)
    while indice < longitud:
        if e == s[longitud - 1 - indice]:
            return longitud - 1 - indice
        indice += 1

#print (ultima_aparcion ([-1,4,0,4,100,0,100,0,-1,-1],0))

# Ejercicio 2
#
#  problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
#    requiere: -
#    asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
#    asegura: {res no tiene elementos repetidos }
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,3,0,100,0,-1,-1]
#   t = [0,100,5,0,100,-1,5]
# se debería devolver res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó res = [4,5,3] 
# ó res = [5,3,4] ó res = [5,4,3]

#defino una funcion auxiliar que me dice si un elemento pertenece o no a una lista


def pertenece (n , l:list) -> bool:
    pertenece = False
    for e in l:
        if e == n:
            pertenece = True
    return pertenece

def pertenece_ambas (e:int,l:list,t:list):
    return pertenece(e,l) and pertenece (e,t)

def elemento_exclusivo (s:list,t:list)->list:
    res:list = []
    syt = s + t
    for e in syt:
        if not pertenece_ambas (e,s,t):
            if not pertenece (e,res):
                res.append(e)
    return res

#print(elemento_exclusivo([-1,4,0,4,3,0,100,0,-1,-1],[0,100,5,0,100,-1,5]))

# Ejercicio 3
#
# Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
# en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
# en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
# palabras que tienen la misma traducción en inglés y en alemán.

#  problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
#    requiere: -
#    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
#  }

#  Por ejemplo, dados los diccionarios
#    aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#    inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#  se debería devolver res=2

# recorro las keys (claves) de ingles y me fijo a la vez si pertenece a la lista de keys (claves) de aleman Y si 
# el valor de la clave en ambas listas es igual. OJO: si pongo los dos operadores logicos en orden inverso (o sea
# digamos si pongo primero la igualdad y luego el pertenece), como no me estoy asegurando de que la clave EXISTE
# en el diccionario de palabras en aleman, el programa SE ROMPE o algo asi en realidad no se bien que pasa pero
#  no esta bueno.

#def contar_traducciones_iguales(ingles: dict, aleman: dict) -> int:
#    res:int = 0
#    for palabra in ingles.keys():
#        if pertenece(palabra,aleman.keys()) and ingles[palabra] == aleman[palabra]:
#            res += 1
#    return res

def contar_traducciones_iguales(ingles:dict,aleman:dict) -> int:
    res:int = 0
    for palabra in ingles.keys():
        if pertenece(palabra,aleman.keys()) and ingles[palabra] == aleman[palabra]:
            res += 1
    return res

#print(contar_traducciones_iguales({"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"},{"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}))

# Ejercicio 4
#
# Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, 
# y sus valores la cantidad de veces que cada uno de esos números aparece en s

#  problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
#    requiere: -
#    asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
#  }

#  Por ejemplo, dada la lista
#  lista = [-1,0,4,100,100,-1,-1]
#  se debería devolver res={-1:3, 0:1, 4:1, 100:2}
#  
# RECORDAR QUE NO IMPORTA EL ORDEN DE LAS CLAVES EN UN DICCIONARIO

# primero defino una funcion auxiliar que me dice cuantas veces aparece un elemento en una lista

def cuantas_veces_aparece (n:int,s:list)->int:
    res:int = 0
    for e in s:
        if e == n:
            res += 1
    return res

def convertir_a_diccionario(lista:list)->dict:
    diccionario:dict = {}
    for e in lista:
        diccionario[e] = cuantas_veces_aparece(e,lista)
    return diccionario

#print(convertir_a_diccionario([-1,0,4,100,100,-1,-1]))

print("FIN PARCIAL 1, ABAJO COMIENZA EL 2")

#1) Índice de la n-ésima aparición [2 puntos]
#Guido y Marcela son dos estudiantes de IP, nervioses con el parcial de Python. 
#Con el objetivo de tener un rato antes del parcial para preguntarse algunas dudas 
#deciden encontrarse en el colectivo y viajar juntes. 
#Para poder coordinar de forma exacta en qué colectivo se tienen que subir, 
#Marcela usa sus habilidades de programación aprendidas en IP para acceder de forma 
#poco legítima a la base de datos de colectivos de todas las empresas. 
#Con esto, arma una lista de todos los colectivos que van a pasar por la parada de
#Guido alrededor del horario acordado y le indica a Guido que se tiene que subir en 
#el 3er colectivo de la línea 34. Por desgracia, Guido se olvida sus lentes antes 
#de salir y no es capaz de distinguir a qué línea pertenece cada colectivo que 
#llega a la parada. Por lo que solo puede contar cantidad total de colectivos que 
#pasan.
#Implementar la función ind_nesima_aparicion que dada una secuencia de enteros s, 
#y dos enteros n y elem devuelve la posición en la cual elem aparece por n-ésima vez 
#en s. En caso de que elem aparezca menos de n veces en s, devolver -1.

#problema ind_nesima_aparicion (in s: seq⟨Z⟩, in n: Z, in elem: Z) : Z {
#  requiere: {n>0}
#  asegura: {Si el elemento aparece menos de n veces en la secuencia, res= -1 }
#  asegura: {Si el elemento aparece al menos n veces en la secuencia, s[res] = elem }
#  asegura: {Si el elemento aparece al menos n veces en la secuencia, elem aparece n-1 
#  veces en s entre las posiciones 0 y res-1 }

#Por ejemplo, dadas
#s = [-1, 1, 1, 5, -7, 1, 3]
#n = 2
#elem = 1
#se debería devolver res = 2


#primero defino una función que me dice cuántas veces aparece un elemento s.

def cuantas_veces_aparece2 (s:list,elem:int)->int:
    contador:int = 0
    for e in s:
        if e == elem:
            contador += 1
    return contador

#con esta funcion defino mi función índice de n-ésima aparición.fíjense que si elem aparece
#menos de n veces la función se saltea el ciclo if y devuelve directamente res (que definí -1).

# def ind_nesima_aparicion(s: list, n: int, elem: int) -> int:
#     indice: int = 0
#     contador: int = 0
#     res: int = -1
#       if cuantas_veces_aparece(s,elem) >= n:
#           while contador < n:
#                if s[indice] == elem:
#                  contador = contador + 1
#                       indice = indice + 1
#             res = res + 1
# return res


def ind_nesima_aparicion (s:list,n:int,elem:int)->int:
    indice: int = 0
    contador: int =0
    res: int = -1
    if cuantas_veces_aparece2 (s,elem) >= n:
        while contador < n:
            if s[indice] == elem:
                contador += 1
            indice += 1
            res += 1
    return res

#print(ind_nesima_aparicion ([-1, 1, 1, 5, -7, 1, 3],2,1))

#2) Mezclar [2 puntos]
#A la hora de jugar juegos de cartas, como el truco, el tute, o el chinchón, 
#es importante que la distribución de las mismas en el mano sea aleatoria. 
#Para esto, al comienzo de cada mano, antes de repartir las mismas se realizan 
#mezclan sucesivas. Una técnica de mezclado es la denominada "mezcla americana" 
#que consiste en separar el mazo en (aproximadamente) dos mitades e intercalar 
#las cartas de ambas mitades. Implementar la función mezclar que dadas dos listas 
#s1 y s2 con igual cantidad de elementos devuelva una lista con los elementos 
#intercalados. Esto es, las posiciones pares de res tendrán los elementos de s1 
#y las posiciones impares los elementos de s2, respetando el orden original.

#problema mezclar (in s1: seq⟨Z⟩, in s2: seq⟨Z⟩) : seq⟨Z⟩ {
#  requiere: {|s1| = |s2| }
#  asegura: {|res| = 2 * |s1|}
#  asegura: {res[2*i] = s1[i] y res[2*i+1] = s2[i], para i entre 0 y |s1|-1}
#}
#TIP: realizar la iteración mediante índices y no mediante elementos

#Por ejemplo, dadas
#s1 = [1, 3, 0, 1]
#s2 = [4, 0, 2, 3]
#se debería devolver res = [1, 4, 3, 0, 0, 2, 1, 3]


#encaro el problema de una sin funciones auxiliares. defino un
#índice general (para iterar) y un índice para cada lista de enteros.
#también defino una lista ambos que es la suma de las dos listas para usar
#de break en el while. básicamente lo que hace mi programa es fijarse si
#el índice general es más chico que la cantidad de elementos de ambas listas 
#sumadas, y luego, dependiendo de si este índice es par o impar (me fijo esto 
#con la operación módulo, el %), agrego a mi lista res (la que va a devolver mi
#función) el elemento de la lista que corresponda. por último le sumo 1 a indice
#para que en la próxima iteración vaya a la otra lista, y le sumo 1 al índice 
#de la lista para que "avance" a lo largo de la lista.


# def mezclar(s1: list, s2: list) -> list:
#     res: list = []
#     indice: int = 0
#     indices1: int = 0
#     indices2: int = 0
#     ambos: list = s1 + s2
#     while indice < len(ambos):
#         if indice % 2 == 0:
#             res.append(s1[indices1])
#             indices1 = indices1 + 1
#             indice = indice + 1
#         if indice % 2 == 1:
#             res.append(s2[indices2])
#             indices2 = indices2 + 1
#             indice = indice + 1
#     return res

def mezclar(s1:list, s2:list)->list:
    res:list = []
    indice: int = 0
    indice1: int = 0
    indice2: int = 0
    ambos: list = s1 + s2
    while indice < len(ambos):
        if indice % 2 == 0:
            res.append(s1[indice1])
            indice1 += 1
            indice += 1
        if indice % 2 == 1:
            res.append(s2[indice2])
            indice2 += 1
            indice += 1
    return res

#print(mezclar([1, 3, 0, 1],[4, 0, 2, 3]))

#3) A los pingos: resultado carreras [3 puntos]
#Además de recitales de artistas de renombre internacional (ej: Bizarrap), 
#en el hipódromo de Palermo se realizan cotidianamente carreras de caballos. 
#Por ejemplo, durante el mes de Octubre se corrieron 10 carreras. En cada una de
#ellas participaron alrededor de 10 caballos.
#Implementar la función frecuencia_posiciones_por_caballo que dada la lista de 
#caballos que corrieron las carreras, y el diccionario que tiene los resultados del 
#hipódromo en el formato carreras:posiciones_caballos, donde carreras es un String 
#y posiciones_caballos es una lista de strings con los nombres de los caballos, 
#genere un diccionario de caballos:#posiciones, que para cada caballo devuelva la 
#lista de cuántas veces salió en esa posición.

#Tip: para crear una lista con tantos ceros como caballos se puede utilizar la siguiente 
#sintaxis lista_ceros = [0]*len(caballos)

#problema frecuencia_posiciones_por_caballo(in caballos: seq⟨String⟩, in carreras: 
#dict⟨String,seq⟨String⟩⟩: dict⟨String,seq⟨Z⟩⟩ {
#  requiere: {caballos no tiene repetidos}
#  requiere: {Los valores del diccionario carreras son permutaciones de la lista 
#  caballos (es decir, tienen exactamente los mismos elementos que caballos, en 
#  cualquier orden posible)}
#  asegura: {res tiene como claves los elementos de caballos}
#  asegura: {El valor en res de un caballo es una lista que indica en la posición i 
#  cuántas veces salió ese caballo en la i-ésima posición.}
#}
#Por ejemplo, dados
#caballos= ["linda", "petisa", "mister", "luck" ]
#carreras= {"carrera1":["linda", "petisa", "mister", "luck"],
#                  "carrera2":["petisa", "mister", "linda", "luck"]}
#se debería devolver res = {"petisa": [1,1,0,0],
#                                          "mister": [0,1,1,0],
#                                          "linda": [1,0,1,0],
#                                          "luck": [0,0,0,2]}


#primero defino una función que me dice en qué posición salio un
#caballo determinado en una carrera.

def posicion(caballo:str, lista:list) -> int:
    indice: int = 0
    for e in lista:
        if e == caballo:
            return indice
        indice = indice + 1

#ahora defino una función que, pasándole el nombre de un caballo y un diccionario
#con carreras, me arma una lista de enteros que dice cuántas veces salió ese
#caballo en cada posición. 

# def posiciones(caballo: str, carreras: dict) -> [int]:
#     lista_carreras: list = []
#     for carrera in carreras.keys():
#         lista_carreras.append(carreras[carrera])
#     primera_carrera: list = lista_carreras[0]
#     caballos: int = len(primera_carrera)
#     res: list = [0] * caballos
#     for lista in lista_carreras:
#         res[posicion(caballo,lista)] = res[posicion(caballo,lista)] + 1
#     return res

def posiciones(caballo:str, carreras:dict)-> list[int]:
    lista_carreras: list = []
    for carrera in  carreras.keys():
        lista_carreras.append(carreras[carrera])
    primera_carrera: list = lista_carreras[0]
    caballos: int = len(primera_carrera)
    res : list = [0] * caballos
    for lista in lista_carreras:
        res[posicion(caballo,lista)] = res[posicion(caballo,lista)] + 1
    return res

# ahora itero en la lista de caballos y a cada uno le pregunto cuántas veces
# salió en cada posición (usando la función posiciones).

# def frecuencia_posiciones_por_caballo(caballos: list, carreras: dict) -> dict:
#     res: dict = {}
#     for caballo in caballos:
#         res[caballo] = posiciones(caballo, carreras)
#     return res

def frecuencia_posisciones_por_caballo(caballos:list, carreras:dict)-> dict:
    res : dict = {}
    for caballo in caballos:
        res[caballo] = posiciones(caballo, carreras)
    return res

#print(frecuencia_posisciones_por_caballo(["linda", "petisa", "mister", "luck" ],{"carrera1":["linda", "petisa", "mister", "luck"],"carrera2":["petisa", "mister", "linda", "luck"]}))

#4) Matriz capicúa [3 puntos]
#Implementar la función matriz_capicua que dada una matriz devuelve True si 
#cada una de sus filas es capicúa. Es decir, si cada fila es igual leída de 
#izquierda a derecha o de derecha a izquierda. Definimos a una secuencia de
#secuencias como matriz si todos los elemento de la primera secuencia tienen 
#la misma longitud.

#problema matriz_capicua(in m:seq⟨seq⟨Z⟩⟩ ) : Bool {
#  requiere: {todos los elementos de m tienen igual longitud (los elementos de m son secuencias)}
#  asegura: {(res = true) <=> todos los elementos de m son capicúa}
#}

#Por ejemplo, dada la matriz
#m = [[1,2,2,1],[-5,6,6,-5],[0,1,1,0]]
#se debería devolver res = true



#primero defino una función que me dice si una lista es capicúa. como mi matriz
#va a estar representada como una lista de listas esta función es bastante útil.

def lista_capicua (lista:list) -> bool:
    lista_capicua: bool = True
    largo: int = len(lista)
    indice1: int = 0
    indice2: int = largo - 1
    while indice1 <= indice2:
        if lista[indice1] != lista [indice2]:
            lista_capicua = False
        indice1 = indice1 + 1
        indice2 = indice2 - 1
    return lista_capicua



def matriz_capicua(m:list)->bool:
    matriz_capicua: bool = True
    for lista in m:
        if not lista_capicua(lista):
            matriz_capicua = False
    return matriz_capicua

#print(matriz_capicua ([[1,2,2,1],[-5,6,6,-5],[0,1,1,0],[1,2,2,1],[-5,6,6,-5],[0,1,1,0],[1,2,2,1],[-5,6,6,-5],[0,1,1,0]]))

print("FIN PARCIAL 2, ABAJO COMIENZA EL 3")

def reordenar_cola_priorizando_vips(filasClientes:Cola[str,str]) -> Cola[str]:
    cola_copiada:Cola = Cola()
    cola_copiada_aux:Cola = Cola()
    clientes_vip:Cola = Cola()
    clientes_comunes:Cola = Cola()
    clientes_ordenados:Cola = Cola()
    
    while not (filasClientes.empty()):
        elem = filasClientes.get()
        cola_copiada.put(elem)
        cola_copiada_aux.put(elem)
    
    while not (cola_copiada.empty()):
        cliente = cola_copiada.get()
        if cliente[1] == "vip":
            clientes_vip.put(cliente)
        elif cliente[1] == "comun":
            clientes_comunes.put(cliente)
    
    while not cola_copiada_aux.empty():
        cliente = cola_copiada_aux.get()
        filasClientes.put(cliente)
    
    while not (clientes_vip.empty()):
        cliente = clientes_vip.get()
        clientes_ordenados.put(cliente)
    
    while not (clientes_comunes.empty()):
        cliente = clientes_comunes.get()
        clientes_ordenados.put(cliente)
    
    return clientes_ordenados

# filaClientes: Cola = Cola()
# filaClientes.put(("juan", "vip")) #1
# filaClientes.put(("ana", "vip")) #2
# filaClientes.put(("seba", "comun")) #5
# filaClientes.put(("rodo", "vip")) #3
# filaClientes.put(("aejo", "comun")) #6
# filaClientes.put(("leo", "comun")) #7
# filaClientes.put(("bale", "vip")) #4
# print(filaClientes.queue)
# print(reordenar_cola_priorizando_vips(filaClientes).queue)
# print(filaClientes.queue)

# 2) Chicken Game (3 puntos)
# El juego del gallina es una competición en la que dos participantes conducen un vehículo en dirección al del contrario; si
# alguno se desvía de la trayectoria de choque pierde y es humillado por comportarse como un "gallina". Se hizo un torneo
# para ver quién es el menos gallina. Juegan todos contra todos una vez y van sumando puntos, o restando. Si dos jugadores 
# juegan y se chocan entre sí, entonces pierde cada uno 5 puntos por haberse dañado. Si ambos jugadores se desvían, pierde
# cada uno 10 puntos por gallinas. Si uno no se desvía y el otro sí, el gallina pierde 15 puntos por ser humillado y el ganador
# suma 10 puntos! En este torneo, cada persona que participa tiene una estrategia predefinida para competir: o siempre se 
# desvía, o nunca lo hace. Se debe programar la función 'torneo_de_gallinas' que recibe un diccionario (donde las claves
# representan los nombres de los participantes que se anotaron en el torneo, y los valores sus respectivas estrategias) y 
# devuelve un diccionario con los puntajes obtenidos por cada jugador.

# problema torneo_de_gallinas(in estrategias: dict<String, String>) : dict<String,Z> {
# requiere: {estrategias tiene por lo menos 2 elementos(jugadores)}
# requiere: {Las claves de estrategias tienen longitud mayor a 0}
# requiere: {Los valores de estrategias sólo pueden ser los strings "me desvío siempre" ó "me la banco y no me desvío"}
# asegura: {Las claves de res y las claves de estrategias son iguales}
# asegura: {para cada jugador p perteneciente a claves(estrategias), res[p] es igual a la cantidad de puntos que obtuvo al
# finalizar el torneo, dado que jugó una vez contra cada otro jugador}
# }

def torneo_de_gallinas(estrategias:dict[str,str]) -> dict[str,int]:
    puntajes: dict[str,int] = {}
    
    for jugador in estrategias.items():
        if jugador not in puntajes.keys():
            puntajes[jugador[0]] = 0
        for contrincante in estrategias.items():
            if jugador != contrincante:
                if jugador[1] == "me desvío siempre" and contrincante[1] == "me desvío siempre":
                    puntajes[jugador[0]] -= 10
                elif jugador[1] == "me la banco y no me desvío" and contrincante[1] == "me la banco y no me desvío":
                    puntajes[jugador[0]] -= 5
                elif jugador[1] == "me la banco y no me desvío" and contrincante[1] == "me desvío siempre":
                    puntajes[jugador[0]] += 10
                elif jugador[1] == "me desvío siempre" and contrincante[1] == "me la banco y no me desvío":
                    puntajes[jugador[0]] -= 15
    
    return puntajes

e1 = {"leo": "me desvío siempre", "rodo": "me la banco y no me desvío"}
# leo = -15
# rodo = 10
#print(torneo_de_gallinas(e1))
e2 = {"leo": "me desvío siempre", "rodo": "me la banco y no me desvío", "bale": "me desvío siempre"}
# leo = -25
# rodo = 20
# bale = -25
#print(torneo_de_gallinas(e2))
e3 = {"leo": "me desvío siempre", "rodo": "me la banco y no me desvío", "bale": "me desvío siempre", "nico": "me la banco y no me desvío"}
# leo = -40
# rodo = 15
# bale = -40
# nico = 15
#print(torneo_de_gallinas(e3))
e4 = {"leo": "me desvío siempre", "rodo": "me la banco y no me desvío", "bale": "me desvío siempre", "nico": "me la banco y no me desvío", "ale": "me la banco y no me desvío"}
# leo = -55 
# rodo = 10
# bale = -55
# nico = 10
# ale = 10
#print(torneo_de_gallinas(e4))

# 3) Cuasi Ta-Te-Ti (2 puntos)
# Ana y Beto juegan al Ta-Te-Ti-Facilito. El juego es en un tablero cuadrado de lado entre 5 y 10. Cada jugador va poniendo su
# ficha en cada turno. Juegan intercaladamente y comienza Ana. Ana pone siempre una "X" en su turno y Beto pone una "O" en 
# el suyo. Gana la persona que logra poner 3 fichas suyas consecutivas en forma vertical. SI el tablero está completo y no ganó
# nadie, entonces se declara un empate. El tablero comienza vacío, representado por " " en cada posición.
# Notar que dado que juegan por turnos y comienza Ana poniendo una "X" se cumple que la cantidad de "X" es igual a la 
# cantidad de "O" o bien la cantidad de "X" son uno más que la cantidad de "O".
# Se nos pide implementar una función en python 'problema_quien_gano_el_tateti_facilito' que determine si ganó alguno, o si
# Beto hizo trampa (puso una 'O' cuando Ana ya había ganado).

# problema quien_gano_el_tateti_facilito(in tablero: seq<seq<Char>>) : Z{
# requiere: {tablero es una matriz cuadrada}
# requiere: {5 <= |tablero[0]| <= 10]}
# requiere: {tablero sólo tiene 'X', 'O' y '' (espacio vacío) como elementos}
# requiere: {En tablero la cantidad de 'X' es igual a la cantidad de 'O' o bien la cantidad de 'X' es uno más que la cantidad de
# 'O'}
# asegura: {res = 1 <==> hay tres 'X' consecutivas en forma vertical (misma columna) y no hay tres 'O' consecutivas en forma
# vertical(misma columna)}
# asegura: {res = 0 <==> no hay tres 'O' ni hay tres 'X' consecutivas en forma vertical}
# asegura: {res = 3 <==> hay tres 'X' y hay tres 'O' consecutivas en forma vertical (evidenciando que beto hizo trampa)}
# }


def hay_tres_iguales(lista: list[int]) -> bool: # hago una funcion que lea si en una lista hay 3 elementos iguales
    res = bool
    indice: int = 0
    for i in range(len(lista)): # recorro la lista
        numero: int = lista[i] # veo cada numero en particular 
        contador_iguales: int = 0 # restauro el contador
        indice: int = 0 # restauro el indice
        while indice < len(lista):
            if numero == lista[indice]:
                contador_iguales += 1 # por cada numero igual sumo uno al contador
                if contador_iguales == 3:
                    return True # si el contador llega a 3 devuelve True
                indice += 1
            else:
                indice += 1
    return False # si no encuentra 3 elementos iguales devuelve False

def quien_gano_el_tateti_facilito(tablero: list[str]) -> int:
    indices_x: list[int] = []
    indices_o: list[int] = []
    res_x = bool
    res_o = bool
    for filas in range(len(tablero)): # recorro cada fila del tablero
        for columnas in range(len(tablero[filas])): # recorro lo equivalente a cada columna del tablero
            if tablero[filas][columnas] == "X":
                indices_x.append(columnas) # si encuentra una X pongo el indice en indices_x
            elif tablero[filas][columnas] == "O":
                indices_o.append(columnas) # si encuentra una O pongo el indice en indices_o
    if hay_tres_iguales(indices_x):
        res_x = True
    else:
        res_x = False
    if hay_tres_iguales(indices_o):
        res_o = True
    else:
        res_o = False
    
    if res_x and res_o == False:
        return 1
    
    if res_x == False and res_o == False:
        return 2
    
    if res_x and res_o:
        return 3

t = [["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""]]
t1 = [["X","","O","",""],["X","O","","",""],["X","","","","O"]] #1
#print(quien_gano_el_tateti_facilito(t1))
t2 = [["","O","","","",""],["","X","","","O",""],["","X","","","",""],["","X","O","","",""]]
#print(quien_gano_el_tateti_facilito(t2)) #1
t3 = [["","O","","X","",""],["","","O","","","X"],["","O","","","",""],["X","","","","",""]]
#print(quien_gano_el_tateti_facilito(t3)) #2
t4 = [["","O","","X","",""],["","","O","","","X"],["","","","","O",""],["X","","","","",""]]
#print(quien_gano_el_tateti_facilito(t4)) #2
t5 = [["","X","","","","","O"],["X","","O","","","",""],["","","","","O","X","X"],["O","","","","","","X"]] #2
#print(quien_gano_el_tateti_facilito(t5))
t6 = [["X","","","","",""],["X","","","O","",""],["X","","","O","",""],["","","","O","",""]] #3
#print(quien_gano_el_tateti_facilito(t6))
t7 = [["","","","","","O"],["","","X","O","",""],["X","O","X","","",""],["","","X","","","O"]] #1
#print(quien_gano_el_tateti_facilito(t7))


# 4) Cuántos palíndromos sufijos (2 puntos)
# Decimos que una palabra es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda. Se nos pide
# programar en python la siguiente función:

# problema cuantos_sufijos_son_palindromos(in texto:String) : Z{
# requiere: -
# asegura: {res es igual a la cantidad de palíndromos que hay en el conjunto de sufijos de texto}
# }

# Nota: un sufijo es una subsecuencia de texto que va desde una posición cualquiera hasta el final de la palabra. Ej: "Diego",
# el conjunto de sufijos es: "Diego", "iego", "ego", "go", "o". Para este ejercicio no consideramos a "" como sufijo de ningún
# texto.

def es_palindromo(palabra:str) -> bool:
    res = bool
    for i in range(len(palabra)):
        if palabra[i] == palabra[len(palabra) - i - 1]:
            res = True
        else:
            return False
    return res

def sacar_primera_letra(palabra: str) -> str:
    palabra_nueva: str = ""

    if len(palabra) > 0:
        for i in range(1, len(palabra)):
            palabra_nueva += palabra[i]
    return palabra_nueva

def cuantos_sufijos_son_palindromos(texto: str) -> int:
    cantidad_sufijos: int = 0

    while len(texto) > 0:
        if es_palindromo(texto):
            cantidad_sufijos += 1
            texto = sacar_primera_letra(texto)
        else:
            texto = sacar_primera_letra(texto)
    return cantidad_sufijos

# print(cuantos_sufijos_son_palindromos("diego")) #1
# print(cuantos_sufijos_son_palindromos("asgus")) #1
# print(cuantos_sufijos_son_palindromos("hannah")) #2
# print(cuantos_sufijos_son_palindromos("anana")) #3

print("FIN PARCIAL 3, ABAJO COMIENZA EL 4")

# 1) Atención por guardia (1 punto)
# Desde el Hospital Fernandez nos pidieron solucionar una serie de problemas relacionados con la información que maneja
# sobre los pacientes y el personal de salud. En primer lugar debemos resolver en qué orden se deben atender los pacientes
# que llegan a la guardia. En enfermería, hay una primera instancia que clasifica en dos colas a los pacientes: una urgente y
# otra postergable (esto se llama hacer triage). A partir de dichas colas que contienen la identificación del paciente, se pide
# devolver una nueva cola según la siguiente especificación.

# problema orden_de_atencion (in urgentes: cola <Z>, in postergables: cola <Z>): cola <Z> {
# requiere: {no hay elementos repetidos en urgentes}
# requiere: {no hay elementos repetidos en postergables}
# resquiere: {la intersección entre postergables y urgentes es vacía}
# requiere: {|postergables| = |urgentes|}
# asegura: {no hay repetidos en res}
# asegura: {res es permutación de la concatenación de urgentes y postergables}
# asegura: {Si urgentes no es vacía, en tope de res hay un elemento de urgentes}
# asegura: {En res no hay dos seguidos de urgentes}
# asegura: {En res no hay dos seguidos de postergables}
# asegura: {Para todo c1 y c2 de tipo "urgente" pertenecientes a urgentes si c1 aparece antes que c2 en urgentes entonces c1
# aparece antes que c2 en res}
# asegura: {Para todo c1 y c2 de tipó "postergable" pertenecientes a postergables si c1 aparece antes que c2 en postergables
# entonces c1 aparece antes que c2 en res}
# }


def orden_de_atencion(urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
    urgentes_copia: Cola[int] = Cola() # hago una copia de la cola de urgentes
    urgentes_aux: Cola[int] = Cola() # se puede hacer con una sola copia de la cola original pero me quiero asegurar
    postergables_copia: Cola[int] = Cola() # hago una copia de la cola de postergables
    postergables_aux: Cola[int] = Cola() # hago una copia de postergables
    cola_ordenada: Cola[int] = Cola() # se puede hacer con una sola copia de la cola original pero me quiero asegurar

    while not urgentes.empty(): # saco los elementos de urgentes para meterlos a las otras dos colas auxiliares
        paciente: int = urgentes.get()
        urgentes_copia.put(paciente)
        urgentes_aux.put(paciente)
    
    while not postergables.empty(): # saco los elementos de postergables para meterlos a las otras dos colas auxiliares
        paciente: int = postergables.get()
        postergables_copia.put(paciente)
        urgentes_aux.put(paciente)

    while not urgentes_aux.empty(): # restauro los elementos de urgentes
        paciente = urgentes_aux.get()
        urgentes.put(paciente)

    while not postergables_aux.empty(): # restauro los elementos de postergables
        paciente = postergables_aux.get()
        postergables.put(paciente)

    while not urgentes_copia.empty() and not postergables_copia.empty(): # ahora debo meter los elementos de urgentes y postergables al res
        urgente: int = urgentes_copia.get()
        cola_ordenada.put(urgente) # primero pongo un elemento de urgentes
        postergable: int = postergables_copia.get()
        cola_ordenada.put(postergable) # luego pongo un elemento de postergables
    
    return cola_ordenada.queue # para el resultado no sé si va cola_ordenada o cola_ordenada.queue, pero con .queue se pueden ver los elementos

urgentes = Cola()
urgentes.put(1)
urgentes.put(2)
urgentes.put(3)
#print(urgentes.queue)
postergables = Cola()
postergables.put(4)
postergables.put(5)
postergables.put(6)
#print(postergables.queue)
#print(orden_de_atencion(urgentes, postergables))

# 2) Alarma epidemiológica (3 puntos)
# Necesitamos detectar la aparición de posibles epidemias. Para esto contamos con una lista de enfermedades infecciosas y
# los registros de atención por guardia dados por una lista de expedientes. Cada expediente es una tupla con ID paciente y
# enfermedad que motivó la atención. Debemos devolver un diccionario cuya clave son las enfermedades infecciosas y su
# valor es la proporción de pacientes que se atendieron por esa enfermedad. En este diccionario deben aparecer solo 
# aquellas enfermedades infecciosas cuya proporción supere cierto umbral.

# problema alarma_epidemiologica(registros: seq<ZxString>, infecciosas: seq<String>, umbral: R): dict<String,R>{
# requiere: {0 < umbral < 1}
# asegura: {claves de res pertenecen a infecciosas}
# asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa
# enfermedad sobre el total de registros es mayor o igual al umbral, entonces res[enfermedad] = porcentaje}
# asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa
# enfermedad sobre el total de registros es menor que el umbral, entonces enfermedad no aparece en res}
# }

def alarma_epidemiologica(registros: list[(int, str)], infecciosas: list[str], umbral: float) -> dict[str, float]:
    res: dict[str, float] = {}
    enf_totales: int = len(registros) # necesito este numero para calcular el porcentaje

    for enfermedad in infecciosas: # recorro la lista de registros
        atendidos_enfermedad: int = 0
        porcentaje: float = 0.0
        for i in range(len(registros)):
            if registros[i][1] == enfermedad: # veo si el segundo elemento de la tupla coincide con la enfermedad
                atendidos_enfermedad += 1 # si coinciden, sumo 1 al contador atendidos_enfermedad
        porcentaje = (atendidos_enfermedad/(enf_totales)) # calculo el porcentaje de la enfermedad
        if porcentaje > umbral:
            if enfermedad not in res:
                res[enfermedad] = porcentaje # si el porcentaje supera al umbral, lo agrego al diccionario del resultado
    return res

registros = [(111,"sifilis"),(222,"sifilis"),(333,"neumonia"),(444,"sifilis"),(555,"neumonia"),(666,"lolero")]
infecciosas = ["sifilis", "neumonia", "lolero"]
umbral = 0.3
#print(alarma_epidemiologica(registros, infecciosas, umbral))
registros1 = [(111,"sifilis"),(222,"sifilis"),(333,"sifilis"),(444,"lolero"),(555,"gripe"),(666,"gripe"),(777,"neumonia"),(888,"neumonia"),(999,"gripe")]
infecciosas1 = ["sifilis", "neumonia", "lolero"]
umbral1 = 0.3
#print(alarma_epidemiologica(registros1, infecciosas1, umbral1))

# 3) Empleados del mes (2 puntos)
# Dado un diccionaio con la cantidad de horas trabajadas por empleado, en donde la clave es el ID del empleado y el valor es
# una lista de las horas trabajadas por día, queremos saber quienes trabajaron más para darles un premio. Se deberá buscar
# la o las claves para la cual se tiene el máximo valor de cantidad total de horas, y devolverlas en una lista.

# problema empleados_del_mes(horas: dicc<Z,seq<Z>>): seq<Z> {
# requiere: {No hay valores en horas que sean listas vacías}
# asegura: {Si ID pertenece a res entonces ID pertenece a las claves de horas}
# asegura: {Si ID pertenece a res, la suma de sus valores de horas es el máximo de la suma de elementos de horas de todos
# los otros IDs}
# asegura: {Para todo ID de claves de horas, si la suma de sus valores es el máximo de la suma de elementos de horas de los
# otros IDs, entonces ID pertenece a res}
# }

def empleados_del_mes(horas: dict[int, list[int]]) -> list[int]:
    indice: int = 0
    cantidad_horas: int = 0
    suma_horas: dict[int, int] = {} # hago un diccionario paralelo para poner el trabajador y el total de horas trabajadas
    mismo_max: list[(int,int)] = []
    tupla_max: list[(int,int)] = []
    lista_max: list[int] = []

    for empleado in horas.items(): # recorro las claves e indices del diccionario horas
        cantidad_horas = 0
        indice = 0
        while indice < len(empleado[1]): # empleado[1] se refiere a la lista de horas trabajadas
            cantidad_horas += empleado[1][indice] # sumo cada hora al contador cantidad_horas
            suma_horas[empleado[0]] = cantidad_horas # voy actualizando la cantidad de horas trabajadas del empleado en suma_horas
            indice += 1
    
    max_horas: int = 0 # introduzco la variable max_horas
    for empleado in suma_horas.items(): # recorro las claves e indices de suma_horas
        if empleado[1] > max_horas: # empleado[1] se refiere a la cantidad de horas totales
            max_horas = empleado [1] 
            max_trabajador = empleado[0] # empleado[0] se refiere al trabajador en si
        elif empleado[1] == max_horas:
            mismo_max.append((empleado[0],empleado[1])) # si hay dos empleados con el mismo maximo, los sumo a una lista de mismo_max
    tupla_max.append((max_trabajador,max_horas)) # sumo a otra lista la tupla del trabajador con la mayor cantidad de horas trabajadas 
    lista_max.append(max_trabajador) # sumo a lista_max el ID del trabajador final con la mayor cantidad de horas

    for i in range(len(mismo_max)): # recorro la lista de mismo_max
        if mismo_max[i][1] == tupla_max[0][1]: # comparo el segundo elemento de cada tupla de mismo_max con el segundo elemento de tupla_max
            if mismo_max[i][0] not in lista_max: # evito repeticiones
                lista_max.append(mismo_max[i][0]) 
    
    return lista_max

# h1 = {"111": [1, 2, 3], "222": [2, 3, 4], "333": [4,5,6]}
# print(empleados_del_mes(h1)) #["333"]
# h2 = {"111": [1, 2, 3], "222": [2, 3, 4], "333": [4,5,6], "444": [4,5,6]}
# print(empleados_del_mes(h2)) #["333","444"]
# h3 = {"111": [1, 2, 3], "444": [6,7,8], "222": [2, 3, 4], "333": [4,5,6]}
# print(empleados_del_mes(h3)) #["444"]
# h4 = {"111": [1, 2, 3], "444": [6,7,8], "222": [8,9,10], "333": [4,5,6], "444": [8,9,10], "555": [6,7,8]}
# print(empleados_del_mes(h4)) #["222","444"] o ["444","222"] (en los asegura no se habla del orden)

#--------------------------------------------------------------------------------

# 4) Nivel de ocupacion del hospital
# Queremos saber qué porcentaje de ocupación de camas hay en el hospital. El hospital se representa por una matriz en
# donde las filas son los pisos, y las columnas son las camas. Los valores de la matriz son booleanos que indican si la cama
# está ocupada o no. Si el valor es verdadero (True) indica que la cama está ocupada. Se nos pide programar en python una
# función que devuelve una secuencia de enteros, indicando la proporción de camas ocupadas en cada piso.

# problema nivel_de_ocupacion(camas_por_piso: seq<Seq<Bool>>): seq<R> {
# requiere: {Todos los pisos tienen la misma cantidad de camas}
# requiere: {Hay por lo menos 1 piso en el hospital}
# requiere: {Hay por lo menos una cama por piso}
# asegura: {|res| = |camas|}
# asegura: {Para todo 0 <= i < |res| se cumple que res[i] es igual a la cantidad de camas ocupadas del piso i dividido del total
# de camas del piso i}
# }

def nivel_de_ocupacion(camas_por_piso: list[list[bool]]) -> list[float]:
    lista_porcentajes: list[float] = []
    camas_totales_fila: int = len(camas_por_piso[0]) # como todos los pisos tienen la misma cantidad de camas, da igual el indice elegido

    for filas in range(len(camas_por_piso)): # recorro camas_por_piso
        camas_ocupadas_fila: int = 0
        for columna in camas_por_piso[filas]: # la columna representa cada cama
            if columna == True:
                camas_ocupadas_fila += 1
        lista_porcentajes.append((camas_ocupadas_fila/camas_totales_fila)*100) # el porcentaje se puede hacer sin el *100
    return lista_porcentajes

cp1 = [[True, True, False],
    [False, True, True]]
#print(nivel_de_ocupacion(cp1))
cp2 = [[True, True, False, True],
    [False, True, True, True],
    [False, False, False, True]]
#print(nivel_de_ocupacion(cp2))
cp3 = [[True, True, False, True],
    [False, True, True, True],
    [False, False, False, True],
    [False, False, False, False]]
#print(nivel_de_ocupacion(cp3))

print("FIN PARCIAL 4, ABAJO COMIENZA EL 5")

# 1) Códigos filtrados [2 puntos]
# El hijo del dueño de la veterinaria, cuya actividad principal es ver tik toks, cree que los productos 
# cuyos código de barras terminimoan en números primos son especialmente auspiciosos y deben ser destacados
# en la tienda. Luego de convencer a su padre de esta idea, solicita una función en python que facilite
# esta gestión.

# Se pide implementar una función que, dada una secuencia de enteros, cada uno representando un código 
# de barras de un producto, cree y devuelva una nueva lista que contenga únicamente aquellos números de 
# la lista original cuyos últimos tres dígitos formen un número primo (por ejemplo, 101, 002 y 011).

# Nota: un número primo es aquel que solo es divisible por si mismo y por 1. Algunos ejemplos de hasta 
# tres dígitos son 2, 3, 4, 101, 103, 107, etc.

# problema filtrar_codigos_primos(in codigos_barra: seq<Z>) : seq<Z> {
# requiere: {Todos los enteros de codigos_barra tienen, por lo menos, 3 dígitos}
# requiere: {No hay elementos repetidos en codigos_barra}
# asegura: {los últimos 3 dígitos de cada uno de los elementos de res forman un número primo}
# asegura: {Todos los elementos de codigos_barra cuyos últimos 3 dígitos forman un número primo 
# están en res}
# asegura: {Todos los elementos de res están en codigos_barra}
# }

def divisores(numero: int) -> list[int]: # hago una funcion que me devuelva una lista con los divisores de un numero
    lista_divisores: list[int] = []
    numero_rango: int = numero + 1

    for i in range(1, numero_rango, 1):
        if numero % i == 0:
            lista_divisores.append(i)
    return lista_divisores

def sacar_primer_numero(numero: int) -> int: # hago una funcion que saque el primer numero de un numero
    numero_str: str = str(numero) # debo transformar el numero a un string
    numero_nuevo: int = ""

    if len(numero_str) > 0:
        for i in range(1, len(numero_str)): # el rango empieza en 1 asi elimina el primer elemento
            numero_nuevo += numero_str[i]
    return numero_nuevo

def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
    lista_primos: list[int] = []
    lista_divisores: list[int] = []

    for i in range(len(codigos_barra)):
        numero: int = codigos_barra[i]
        longitud_numero: int = len(str(numero))
        while longitud_numero != 3: # voy sacando numeros de numero hasta que su longitud sea 3
            numero = sacar_primer_numero(numero)
            longitud_numero: int = len(str(numero))
        numero = int(numero) # transformo en int el numero por si hay numeros como 002, 014
        lista_divisores = divisores(numero) 
        if len(lista_divisores) == 2: # si la lista de divisores es 2, el numero es primo
            numero: int = codigos_barra[i]
            lista_primos.append(numero)
    return lista_primos

c1 = [11111002, 214013, 849032, 38491005]
#print(filtrar_codigos_primos(c1))
c2 = [101, 38435028, 4742019, 95472986]
#print(filtrar_codigos_primos(c2))


# 2) Cambios de stock de stock_productos [2 puntos]

# En la veterinaria "Exacta's pets", al finalizar cada día, el personal registra en papeles los nombres y
# la cantidad actual de los productos cuyo stock ha cambiado. Para mejorar la gestión, desde la dirección
# de la veterinaria han pedido desarrollar una solución en Python que les permita analizar las
# fluctuaciones del stock.

# Se pide implementar una función que reciba una lista de tuplas, donde cada tupla contiene el nombre de 
# un producto y su stock en ese momento. La función debe procesar esta lista y devolver un diccionario 
# que tenga como clave el nombre del producto y como valor una tupla con su mínimo y máximo stock histórico
# registrado.

# problema stock_productos(in stock_cambios: seq<<String X Z>>): dict<String, <Z X Z>>{
# requiere: {Todos los elementos de stock_cambios están formados por un string no vacío y un entero >= 0}
# asegura: {res tiene como claves solo los primeros elementos de las tuplas de stock_cambios (o sea, un
# producto)}
# asegura: {res tiene como claves todos los primeros elementos de las tuplas de stock_cambios}
# asegura: {El valor en res de un producto es una tupla de cantidades. Su primer elemento es la menor 
# cantidad de ese producto en stock_cambios y como segundo valor el mayor}
# }

def stock_productos(stock_cambios: list[(str, int)]) -> dict[str,(int, int)]:
    extremos: dict[str,(int, int)] = {} # creo un diccionario vacio
    
    for tuplas in stock_cambios: # agarro cada tupla de la lista
        producto: str = tuplas[0] # el producto va a ser el primer elemento de la tupla
        if producto not in extremos.keys(): # asi me aseguro que no modifique los min y max
            minimo: int = tuplas[1] # el min va a ser el segundo elemento de la tupla
            maximo: int = tuplas[1] # el max va a ser el segundo elemento de la tupla
            for indice in range(len(stock_cambios)): # recorro stock_cambios
                if stock_cambios[indice][0] == producto: # quiero ver si son el mismo producto
                    if stock_cambios[indice][1] < minimo:
                        minimo = stock_cambios[indice][1]
                    elif stock_cambios[indice][1] > maximo:
                        maximo = stock_cambios[indice][1]
            extremos[producto] = (minimo, maximo) # agrego al diccionario el producto con sus max y min
    return extremos

sc1 = [("galletita", 12),("galletita", 10),("galletita", 1),("hueso",120),("hueso",3),("hueso",10)] #{"galletita":(1,12), "hueso":(3,120)}
print(stock_productos(sc1))
sc2 = [("pato", 12),("pato",0),("pato",13),("collar",300),("collar",20),("collar",17),("comida",100),("comida",29)]
#{"pato":(0,13), "collar":(17,300), "comida": (29,100)}
print(stock_productos(sc2))
sc3 = [("correa", 10),("comida",140),("comida",49),("shampoo",2),("shampoo",39),("shampoo",50)]
#{"correa": (10,10), "comida":(49,140), "shampoo": (2,50)}
print(stock_productos(sc3)) 


#fsasczc 
