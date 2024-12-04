from queue import Queue as Cola
from queue import LifoQueue as Pila
import math
from typing import TypeVar 

T = TypeVar('T')

def pertenece (cadena:list [T], elem:T) -> bool:
    for i in cadena:
        if elem == i:
            return True
    return False

def incrementar(diccionario: dict[int, int], primo: int) -> bool:
    if pertenece(diccionario.keys(), primo):
        diccionario[primo] += 1
    else:
        diccionario[primo] = 1

def es_primo(numero: int) -> bool:
    for valor in range (2, numero):
        if numero % valor == 0: 
            return False
    return True

def crear_pila(elementos):
    pila = Pila()
    for elem in elementos:
        pila.put(elem)
    return pila


def da_vuelta_str(s: str) -> str:
    res: str = ""
    iterador: int = len(s) - 1
    for i in range(len(s)):
        res += s[iterador]
        iterador -= 1
    return res 

#1) Ejercicio 1 [2.25 puntos]

#problema multiplos_de_primos (in v: seq⟨Z⟩) : Diccionario⟨Z, Z⟩ {
#  requiere: { Los elementos de v son positivos }
#  asegura: { Las claves de res son números primos, y cada valor corresponde con la cantidad de números en v tales que ese primo lo divide }
#  asegura: { Si existe un número primo p tal que divide a algún número de v, entonces p es clave de res }
#  asegura: { Los valores de res son positivos }
#}

# Ejercicio 1
def multiplos_de_primos(v: list[int]) -> dict[int,int]:
    res: dict[int, int] = {}
    for elem in v:
        for divisor in range(2, elem+1):
            if es_primo(divisor) and elem % divisor == 0:
                    incrementar(res, divisor)
    return res


#print (multiplos_de_primos ([1,2,3,5,30])) 

#2) Ejercicio 2 [2.25 puntos]

#problema longitud_mas_grande (in A: seq⟨seq⟨Z⟩⟩) : Z {
#  requiere:{ Hay al menos un uno en A }
#  asegura: { Sea v la secuencia de unos más larga que está contenida en algún A[i] para i válido, res es igual a la longitud de v }
#}

# Ejercicio 2
def longitud_mas_grande(A: list[list[int]]) -> int:
    copia: list[list[int]] = A.copy()
    contador:int = 0
    indice:int=0
    for i in copia:

        if contador < contador_lista(i):
            contador = contador_lista(i)
        if contador >= contador_lista(i):
            contador = contador
    return contador


def contador_lista (a:list[int]) -> int:
    contador : int = 0
    contadorAux: int = 0
    indice: int = 0
    for i in a:
        if i == 1:
            contador += 1
        if i != 1:
            if contadorAux < contador:
                contadorAux = contador
            contador = 0
        if contadorAux < contador:
            contadorAux = contador   

    return contadorAux

#print(longitud_mas_grande([[1,1,1,3,1,1,1,1,3,1,1,1,4,1,1,1],[11,1,1,1,1,1,1,2]]))
# res = 6


#3) Ejercicio 3 [2.25 puntos]
#Implementar la especificación resolver_cuentas descrita a continuación.

#problema resolver_cuentas(in p: Pila⟨string⟩ ) : seq⟨Z⟩ {
#  requiere: { Para cada elemento x de p vale esta_bien_formado(x) }
#  asegura: { res[i] es igual al resultado de la operación aritmética representada por el tope de la pila p luego de haber desapilado i elementos, para 0 <= i < longitud de p }
#  asegura: { res tiene la misma cantidad de elementos que p }
#}

#problema esta_bien_formado(in s: string) : Bool {
#  requiere: { - }
#  asegura: { res == True <==> Cada caracter de s es '+', '-' o es un dígito; el último caracter de s es un dígito; no hay dos operadores consecutivos en s (los operadores son '+' y '-') }
#}

# Ejercicio 3
def resolver_cuentas(p: Pila [str]) -> list[str]:
    p_copia: Pila[str] = Pila()
    res: list[str] = []

    while not p.empty():
        cuenta:str = p.get()
        p_copia.put(cuenta)
        res.append(calcular(cuenta)) 

    #restauro pila
    while not p_copia.empty():
        p.put(p_copia.get())
    return res

def calcular(cuenta: str):
    res = 0
    numero_actual = 0
    signo = 1  # 1 para suma, -1 para resta

    for caracter in cuenta:
        if caracter == "+" or caracter == "-":
            # agrego el número actual al resultado acumulado
            res += signo * numero_actual
            numero_actual = 0
            if caracter == "+":
                signo = 1
            else:
                signo = -1
        else:
            numero_actual = numero_actual * 10 + int(caracter)

    # agrego el último número al resultado
    res += signo * numero_actual
    return res


#print (resolver_cuentas (crear_pila (["+2-4", "+7-5-2", "+1+6"])))


#4) Ejercicio 4 [2.25 puntos]

#problema dame_el_que_falta (in s: seq⟨ZxZ⟩): ZxZ {
#  requiere: { El menor número que aparece en alguna tupla de s es igual a 1 }
#  requiere: { Sea n el máximo número que aparece en alguna tupla de s, |s| = n*n-1 }
#  requiere: { s no tiene tuplas repetidas }
#  asegura: { Las compontentes de res son valores entre 1 y n, inclusive }
#  asegura: { res no pertenece a s }
#}

# Ejercicio 4
# Ejercicio 4
def dame_el_que_falta(s: list[tuple[int,int]]) -> tuple[int,int]:
    copia:list[tuple[int,int]] = s.copy()
    res: tuple[int,int] = ()
    for i in s:
        if not pertenece2 (s,(i[1],i[0])):
            res = (i[1],i[0])
        if not pertenece2 (s,(i[0],i[0])):
            res = (i[0],i[0])
    return res

def pertenece2(s: list[tuple[int,int]], t:tuple[int,int]) -> bool:
    res: bool = False
    for i in s:
        if i[0] == t[0] and i[1] == t[1]:
            res = True
    return res


#print(dame_el_que_falta([(1,3),(3,3),(3,1),(3,2),(2,3),(1,2),(2,2),(2,1)]))
# [(1,3),(3,3),(3,1),(3,2),(2,3),(1,2),(1,1),(2,2)] -> (2,1)











def minimo(lista: list[float]) -> float:
    curr_minimo = lista[0]
    
    for numero in lista:
        if numero < curr_minimo:
            curr_minimo = numero

    return curr_minimo

def maximo(lista: list[float]) -> float:
    curr_maximo = lista[0]
    
    for numero in lista:
        if numero > curr_maximo:
            curr_maximo = numero

    return curr_maximo

def cant_apariciones(num: int, lista: list[int]) -> int:
    contador: int = 0
    for i in lista:
        if i == num:
            contador += 1
    return contador

# Ejercicio 1
def cantidad_ap_antes_corte(c: str, s: str) -> int:
    contador: int = 0
    for char in s:
        if char == c:
            contador += 1
        if char == "x":
            return contador
    return contador

def verificar_transacciones(s:str) -> int:
    res: int = (350 * cantidad_ap_antes_corte("r", s)) - (56 * cantidad_ap_antes_corte("v", s))

    while res < 0:
        res += 56
    
    return res

# Ejercicio 2


def valor_minimo(s: list[tuple[float, float]]) -> float:
    lista_primeras_pos: list[float] = []
    
    for item in s:
        lista_primeras_pos.append(item[0])
    
    return minimo(lista_primeras_pos)
    
# Ejercicio 3
def valores_extremos(cotizaciones_diarias: dict[str, list[tuple[int, float]]]) -> dict[str, tuple[float,float]]:
    res: dict[str,tuple[float,float]] = {}
    lista_valores: list[float] = []
    minimum: int = 0
    maximum: int = 0
    for clave in cotizaciones_diarias.keys():
        res[clave] = (0.0,  0.0)
    
    for key in res.keys():
        lista_valores = []
        for i in range(len(cotizaciones_diarias[key])):
            lista_valores.append(cotizaciones_diarias[key][i][1])
        
        minimum = minimo(lista_valores)
        maximum = maximo(lista_valores)
        
        res[key] = (minimum, maximum)
    return res
        

# Ejercicio 4
def  es_sudoku_valido(sudoku: list[list[int]]) -> bool:
    longitud:int = len(sudoku)
    res: bool = True
    for i in range(longitud):
        columna: list[int] = []
        for fila in sudoku:
            columna.append(fila[i])
        
        for numero in columna:
            if (cant_apariciones(numero, columna) > 1 or
                cant_apariciones(numero,sudoku[i]) > 1) and numero != 0:
                res = False
        
    return res


historial = "ssrvvvvsvvsvvv"
print(verificar_transacciones(historial))
temperaturas = [(1.0, 5.2), (10.4, 15.1), (19.7, 28.9), (25.4, 35.6), (-3.1, 1.3)]
print(valor_minimo(temperaturas))
cotizaciones =  {"YPF" : [(1,10),(15, 3), (31,100)], "ALUA" : [(1,0), (20, 50), (31,30)]}
print(valores_extremos(cotizaciones))
m = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 4, 5, 3, 2, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
print(es_sudoku_valido(m))
