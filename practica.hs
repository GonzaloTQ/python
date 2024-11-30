{--problema votosEnBlanco(formulas : seq < String × String >, votos : seq < Z >, cantT otalV otos : Z) : Z{
requiere : {formulasV alidas(formulas)}
requiere : {|formulas| = |votos|}
requiere : { Todos los elementos de votos son mayores o iguales que 0}
requiere : { La suma de todos los elementos de votos es menor o igual a cantT otalV otos}
asegura : {res es la cantidad de votos emitidos que no correspondieron a niguna de las f´ormulas que se presentaron }
}

--}

votosEnBlanco :: [(String,String)] -> [Integer] -> Integer -> Integer
votosEnBlanco _ votosPositivos cantTotalVotos = cantTotalVotos - contarvotosPositivos votosPositivos

contarvotosPositivos ::  [Integer] -> Integer
contarvotosPositivos [] = 0
contarvotosPositivos (y:ys) = y + contarvotosPositivos ys

-- votosEnBlanco [("Juan P´erez","Susana Garc´ıa"), ("Mar´ıa Montero","Pablo Moreno")] [34,56] 100
-- 10

{--problema formulasValidas(formulas : seq < String × String >) : Bool{
requiere : {T rue}
asegura : {(res = true) ↔ formulas no contiene nombres repetidos, es decir que cada candidato est´a en una ´unica f´ormula (no
se puede ser candidato a presidente y a vicepresidente ni en la misma f´ormula ni en f´ormulas distintas) }
}--}

formulasValidas :: [(String,String)] -> Bool
formulasValidas [] = True
formulasValidas ((presidente,vicepresidente):xs)  | presidente == vicepresidente = False  
                                                  | estaContenida (presidente,vicepresidente) xs = False
                                                  | otherwise = formulasValidas xs

estaContenida :: (String,String) -> [(String,String)] -> Bool
estaContenida (_,_) [] = True
estaContenida (v1,v2) ((p1,p2):ps)  | v1 == p1 || v1 == p2 = False
                                    | v2 == p1 || v2 == p2 = False
                                    | otherwise = estaContenida (v1,v2) ps


{--
problema porcentajeDeVotos(presidente : String, formulas : seq < String × String >, votos : seq < Z >) : R{
requiere : {La primera componente de algun elemento de formulas es presidente}
requiere : {formulasV alidas(formulas)}
requiere : {|formulas| = |votos|}
requiere : { Todos los elementos de votos son mayores o iguales que 0}
requiere : { Hay al menos un elemento de votos que es mayor estricto que 0}
asegura : {res es el porcentaje de votos que obtuvo la f´ormula encabezada por presidente sobre el total de votos afirmativos }
}
Para resolver este ejercicio pueden utilizar la siguiente funci´on que devuelve como Float la divisi´on entre dos n´umeros de tipo
Int:
division :: Int → Int → Float
division a b = (fromIntegral a) / (fromIntegral b)
--}

porcentajeDeVotos :: String -> [(String,String)] -> [Integer] -> Float
porcentajeDeVotos presidente formulas votos = division (cantidad presidente formulas votos * 100) (contarvotosPositivos votos) 

cantidad :: String -> [(String, String)] -> [Integer] -> Integer
cantidad _ [] _ = 0
cantidad _ _ [] = 0
cantidad presidente ((candidato,vice):xs) (y:ys)  | presidente == candidato = y
                                                  | otherwise = cantidad presidente xs ys


division :: Integer -> Integer -> Float
division a b = (fromIntegral a) / (fromIntegral b)

{--problema proximoPresidente(formulas : seq < String × String >, votos : seq < Z >) : String{
requiere : {La primera componente de algun elemento de formulas es presidente}
requiere : {formulasV alidas(formulas)}
requiere : {|formulas| = |votos|}
requiere : { Todos los elementos de votos son mayores o iguales que 0}
requiere : { Hay al menos un elemento de votos que es mayor estricto que 0}
requiere : {|formulas| > 0}
asegura : {res es el candidato a presidente de formulas m´as votado de acuerdo a los votos contabilizados en votos}
}
--}


proximoPresidente :: [(String, String)] -> [Integer] -> String
proximoPresidente formulas votos = proximoPresidenteAux formulas formulas votos

proximoPresidenteAux :: [(String, String)] -> [(String, String)] -> [Integer] -> String
proximoPresidenteAux [] _ _ = ""
proximoPresidenteAux ((candidato,vice):[]) _ _ = candidato
proximoPresidenteAux ((c1,v1):(c2,v2):xs) formulas votos | votosCandidato1 >= votosCandidato2 = proximoPresidenteAux ((c1,v1):xs) formulas votos
                                                          | otherwise = proximoPresidenteAux ((c2,v2):xs) formulas votos
                                                        where
                                                            votosCandidato1 = cantidad c1 formulas votos
                                                            votosCandidato2 = cantidad c2 formulas votos


--Funciones utiles

-- inverso de lista
reverso :: [t] -> [t]
reverso [] = []
reverso [x] = [x]
reverso (x:xs) = reverso (xs) ++ [x]

-- pertenece x a lista
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y:ys) = x == y || pertenece x ys

-- quita todos los elementos x que aparecen
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos x (y:ys)  | x==y = quitarTodos x ys
                      | otherwise = y:quitarTodos x ys

-- elimina todos los elementos repetidos de una lista
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs)  | null xs = [x]
                          | pertenece x xs = x : quitarTodos x (eliminarRepetidos xs)
                          | otherwise = x : eliminarRepetidos xs

-- primos

longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

listaDivisores :: Integer -> [Integer]
listaDivisores numero = contar numero
  where
    contar 0 = []
    contar contador
      | mod numero contador == 0 = contador : contar (contador - 1)
      | otherwise = contar (contador - 1)

esPrimo :: Integer -> Bool
esPrimo numero = longitud (listaDivisores numero) == 2

factoresPrimos :: Integer -> [Integer]
factoresPrimos n = factoresPrimosAux n 2

factoresPrimosAux :: Integer -> Integer -> [Integer]
factoresPrimosAux 1 _ = []
factoresPrimosAux m d | m `mod` d == 0 = d : factoresPrimosAux (m `div` d) d
                      | d*d > m = [m]
                      | otherwise = factoresPrimosAux m (d+1)

promedio :: [Integer] -> Float
promedio xs = fromIntegral (suma xs) / fromIntegral (longitud xs)

suma :: [Integer] -> Integer
suma [] = 0
suma (x:xs) = x + suma xs

promedioPrimo :: Integer -> Float
promedioPrimo x = promedio (factoresPrimos x)


cuantosIguales :: [Char] -> [Char] -> Int  
cuantosIguales [] _ = 0
cuantosIguales (' ':xs) y = cuantosIguales xs y
cuantosIguales (x:xs) (y:ys) | x == y = 1 + cuantosIguales (quitarTodos x xs) ys 
                        | otherwise = cuantosIguales xs (y:ys)



