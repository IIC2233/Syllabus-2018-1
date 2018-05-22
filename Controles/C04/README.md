# Control 4

### Parte igual del control
###### (Sólo varía en el orden de las preguntas)

**(2 pts.) Verdadero o Falso**

> - ``property`` es una función _built-in_ que suele utilizarse como decorador.

**Respuesta**: **Verdadero o Falso**.

**Explicación**: Estrictamente hablando, esta no es una función como tal, por lo que si se puso esa argumentación se tomará como correcta. En caso contrario, ``property`` está documentado como un _built-in function_ por lo que si ese era el razonamiento, también se tomará como verdadero.

> - El uso de los siguientes decoradores (ver código) es análogo a la operación ``h(g(f(x)))``.
```python
@h
@g
def f(x):
  pass
```

**Respuesta**: **Verdadero o Falso**

**Explicación**: Para que sea aceptado falso se tomaron en consideración correcciones sintácticas del problema. En particular, si se agrupó de la forma ``h(g(f))(x)``. Otra argumentación _semi-válida_ para poner `False` es que en el enunciado se está llamando la función y en el código más abajo se está sólo definiendo. Este argumento es correcto en ese aspecto, pero no en la definición matemática de las funciones, por lo que se dió la mitad del puntaje. (0.2 pts). De otra manera, se acepta el verdadero

> - En Python, sólo es posible anidar hasta tres definiciones de funciones.

**Respuesta**: **Falso**

**Explicación**: Python no tiene límites en este aspecto. Cualquier explicación en esta dirección se tomó como correcta.

> - En Python, las funciones pueden recibir funciones como argumentos, pero no devolver funciones.

**Respuesta**: **Falso**

**Explicación**: Como se muestra en el material de clases, este es uno de los secretos de los decoradores de Python, el uso de estos es justamente como una función que retorna otra.

> - La función más interna en un decorador **debe** llamarse `wrapper`.

**Respuesta:** **Falso**

**Explicación** Python no requiere nombres especiales para la declaración de decoradores, dado que no hay una palabra reservada (salvo el `@` en la solución "azucarada", pero no es una palabra como tal) por el idioma. En este aspecto se aceptó cualquier explicación que fuera en esta dirección.

**(1 Pt.) Desarrollo Rápido**

> Indique, en un máximo de tres líneas, qué es un decorador en Python y para qué sirve.

**Distribución de puntaje:** El puntaje de esta pregunta se dividió en tres partes:

- 0.3 pts. por decir que era una función
- 0.3 pts. por decir qué retorna, en este caso, otra función
- 0.4 pts. por decir que hacía un decorador.

**Explicación:** En cuanto a para qué sirve, se puede decir que servían para añadir una funcionalidad o modificar el comportamiento al código y **no modificar el mismo**.


**(3 pts.) Lectura de código**

> **1.** Reescriba la función `f1` decorada --como aparece en el código-- **sin utilizar** `@` (_i.e._ sin el azúcar sintáctico). En otras palabras, asuma que `f1` ya está definida y debe emular la funcionalidad añadida en la línea 9.

**Respuesta:** `f1 = decorador(2, 4) (f1)`

**Explicación:** Como verán en el código, esta parte era indiferente a la forma. Básicamente, se está redefiniendo la función `f1`, por lo mismo se debe poner a la izquierda. A la derecha, se le aplica la "función" `decorador()` con parámetros 2 y 4 y que se le aplica a la función `f1`. Por lo mismo, `decorador(2, 4)` retorna una función, la cual recibe `f1` y que seguido de eso retorna una nueva función. Esta última es la "nueva `f1`".

También se aceptaron respuestas que mencionaban que el decorador es un patrón de diseño (muy bien! :D) y que en Python se usaba como una función.

> **2.** Escriba el _output_ del programa.
----------

### Forma 1

```python
def decorador(arg1, arg2=3):
    def _decorador(func):
        def wrapper(*foo, **bar):
            res = func(*foo, **bar)
            return res * arg1 + arg2
        return wrapper
    return _decorador

@decorador(2, 4)
def f1(a, b, c):
    return (a+b)//c

print(f1(4, 3, c=2))
```
- Resultado de ``f1`` = 3
- Al entrar al wrapper se ejecuta 3 * 2 + 4
- Resultado final = 10

----------

### Forma 2

```python
def decorador(arg1, arg2=3):
    def _decorador(func):
        def wrapper(*foo, **bar):
            res = func(*foo, **bar)
            return res * arg1 + arg2
        return wrapper
    return _decorador

@decorador(2, 4)
def f1(a, b, c):
    return (a + b) // c

print(f1(2, 3, c=4))
```
- Resultado de `f1` = 1
- Al entrar al wrapper se ejecuta 1 * 2 + 4
- Resultado final = 6

----------

### Forma 3

```python
def decorador(arg1, arg2=3):
    def _decorador(func):
        def wrapper(*foo, **bar):
            res = func(*foo, **bar)
            return res * arg1 + arg2
        return wrapper
    return _decorador

@decorador(2, 4)
def f1(a, b, c):
    return (a + b) // c

print(f1(5, 2, c=3))
```
- Resultado de `f1` = 2
- Al entrar al wrapper se ejecuta 2 * 2 + 4
- Resultado final = 8
