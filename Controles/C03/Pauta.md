# Control 3

### Verdadero o False (3 puntos)
Cada pregunta vale 0.4 puntos.

1. Las sentencias dentro del bloque `finally` se ejecutan tanto si hubo una excepción como si no.

    **Respuesta:** Verdadero.
2. El _keyword_ `lambda` permite definir funciones anónimas.

    **Respuesta:** Verdadero.

3. Como primer parámetro, `reduce` recibe una función que requiere tres argumentos.

    **Respuesta:** Falso. Recibe una función que toma solo dos argumentos: un acumulador y un valor actual.
    
4. `filter` elimina los elementos que devuelven `True` después de aplicarles la función.

    **Respuesta:** Falso. Elimina los elementos que devuelven `False`, manteniendo los que retornan `True`.

5. El hecho de que un software pase todos los tests significa que no hay errores.

    **Respuesta:** Falso. Los tests unitarios solo sirven para probar casos específicos y por lo tanto, no permiten asegurar que se están cubriendo todas las posibles situaciones.


### Lectura de código (3 pts):

#### Forma A

Escriba el output del programa. Además, escriba el valor de los iteradores instanciados en los pasos previos a la impresión del resultado. Indique a qué generador corresponde cada uno de esos iteradores.


```python
class Node:


ite1 = [3, 1, 4, 1, 5, 9, 2, 6]  # pi
ite2 = [2, 7, 1, 8, 2, 8, 2]     # e
ite3 = [1, 4, 1, 4, 2, 1]        # raíz de 2

resultado = {x[1] * 2 for x in filter(lambda x: x[0] % 2, zip(ite1, ite2, ite3))}
print(resultado)

```

**Respuesta**

Hay tres iteradores que se instancian en los pasos intermedios al obtener `resultado`. Estos son: (1) `z = zip(ite1, ite2, ite3)`, (2) `f = filter(lambda x: x[0] % 2, z)` y (3) el set por comprensión `s = {x[1] * 2 for x in f}`. La principal dificultad que se encontró fue el empleo de la función booleana en el `filter`, la cual a pesar de no entregar un booleano explícito, se _castea_ siguiendo la pista del _hint_: 0 se considera `False` y 1 es `True`.

Con esto, la asignación de puntaje fue la siguiente:
* 1 pto por el resultado correcto del `zip`.
* 0.5 ptos por el correcto empleo de la función booleana de `filter`.
* 1 pto por el resultado de `filter` **para el zip obtenido**.
* 1 pto por los valores obtenidos a partir de `filter` **para el filter obtenido**.
* 0.5 ptos por eliminar duplicados en el resultado final (pues se pedía un set).

Es importante que tanto el `filter` como el `set` se consideraron en base al resultado de la operación anterior, de forma que no se penalizó error de arrastre. Ante errores, se buscó descontar solo en el iterador con problemas.

Se aceptaron varias formas para mostrar los elementos... en este caso, cada iterador se muestra por simplicidad como una tupla con los elementos. Desde luego, hay que recordar que los iteradores **no son tuplas y se muestran así con un fin didáctico**. Los outputs intermedios para el enunciado fueron:

1. zip: `z = ((3, 2, 1), (1, 7, 4), (4, 1, 1), (1, 8, 4), (5, 2, 2), (9, 8, 1))`
2. filter `f = ((3, 2, 1), (1, 7, 4), (1, 8, 4), (5, 2, 2), (9, 8, 1))`
3. set `s = {4, 14, 16}`

#### Forma B

Para el enunciado siguiente,

```python
class Node:



ite1 = [2, 7, 1, 8, 2, 8, 2]     # e
ite2 = [1, 4, 1, 4, 2, 1]        # raíz de 2
ite3 = [3, 1, 4, 1, 5, 9, 2, 6]  # pi

resultado = {x[1] * 3 for x in filter(lambda x: x[2] % 2, zip(ite1, ite2, ite3))}
print(resultado)

```

**Respuesta**

1. zip: `z = ((2, 1, 3), (7, 4, 1), (1, 1, 4), (8, 4, 1), (2, 2, 5), (8, 1, 9))`
2. filter `f = ((2, 1, 3), (7, 4, 1), (8, 4, 1), (2, 2, 5), (8, 1, 9))`
3. set `s = {3, 12, 6}`


#### Forma C

Para el enunciado siguiente,

```python
class Node:



ite1 = [2, 7, 1, 8, 2, 8, 2]     # e
ite2 = [3, 1, 4, 1, 5, 9, 2, 6]  # pi
ite3 = [1, 4, 1, 4, 2, 1]        # raíz de 2

resultado = {x[1] * 4 for x in filter(lambda x: x[1] % 2, zip(ite1, ite2, ite3))}
print(resultado)

```

**Respuesta**

1. zip: `z = ((2, 3, 1), (7, 1, 4), (1, 4, 1), (8, 1, 4), (2, 5, 2), (8, 9, 1))`
2. filter `f = ((2, 3, 1), (7, 1, 4), (8, 1, 4), (2, 5, 2), (8, 9, 1))`
3. set `s = {12, 4, 20, 36}`