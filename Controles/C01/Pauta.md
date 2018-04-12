# Control 1

### Verdadero o False (3 puntos)
1. Un diagrama UML de clases válido requiere que todos los objetos interactúen entre sí.

    **Respuesta**: Falso. No todas las clases tienen que interactuar entre sí en un diagrama de clases. (0.6 puntos)


2. El método `__ call __` permite que un objeto sea llamable.

    **Respuesta**: Verdadero. (0.3 puntos)

3. Una clase A puede heredar de cualquier par de clases B y C, solo si A, B y C son diferentes.

    **Respuesta**: Falso. No siempre se puede determinar un MRO consistente para todas las clases. En tal caso, se obtiene un error al crear la clase. (0.6 puntos)


4. En la instrucción `x=namedtuple('Alumno', 'a b c d')`, la variable `x` es una instancia de la clase `namedtuple`

    **Respuesta**: Falso. "x" es un tipo de objeto o clase llamada "Alumno". (0.6 puntos)


5. Duck Typing entrega comportamiento polimórfico sin utilizar herencia

    **Respuesta**: Verdadero. (0.3 puntos)


6. Si A es una clase abstracta, la sentencia `a=A()` se puede ejecutar solo una vez.

    **Respuesta**: Falso. No es posible instanciar clases abstractas, pero sí subclases. (0.6 puntos)


### Lectura de código (2 puntos)
Escriba el output del código escrito a continuación.
```python
class B:

    def __init__(self, value):
        self.value = value

b0 = B(0)
b1 = B(1)
print(b0.value, b1.value)

b0.value = 3
print(b0.value, b1.value)

b0.value = b1.value
print(b0.value, b1.value)

b1.value = 4
print(b0.value, b1.value)

b0 = b1
print(b0.value, b1.value)

b1.value = 5
print(b0.value, b1.value)
```
**Respuesta**:
```python
0 1 #(0.1 puntos)
3 1 #(0.1 puntos)
1 1 #(0.3 puntos)
1 4 #(0.5 puntos)
4 4 #(0.5 puntos)
5 5 #(0.5 puntos)
```

### Desarrollo rápido (1 punto)
Explique una ventaja de utilizar clases abstractas para el modelamiento por sobre herencia de clases no abstractas. Responda en el espacio asignado.

**Respuesta**: Cualquiera de las opciones sirve.
1. No deja instanciar clases que no "deben" ser instanciadas
2. Permite forzar la implementación de métodos o properties en clases hijas.

**ERRORES COMUNES**: Respuestas repetidas que se vieron en los controles
1. Muchos respondieron que permitía ahorrar código y crear un formato para subclases. Esta no es una ventaja de las clases abstractas, es una ventaja de utilizar herencia.
2. Muchos respondieron que resuelve el problema del diamante. Esto bajo ningún punto de vista es correcto, y se recomienda repasar en qué consiste el problema del diamante, o bien en que consisten las clases abstractas (pues no guardan relación alguna) 
