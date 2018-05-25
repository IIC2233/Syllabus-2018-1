# Pauta Control 5


Este control tiene tres formas distintas, pero son los mismos ítems en distinto orden.

---

### Verdadero y Falso (1.2 pts)

**1)** Una clase es a una instancia lo que una metaclase es a una clase.

**(0.3 pts) R:** Verdadero.


**2)** En Python, `X(arg1, arg2)` es un atajo de `X.__init__(arg1, arg2)`.

**(0.1 pts) R:** Falso.

**(0.2 pts) Justificación:** Es un atajo de `X.__call__(arg1, arg2)`.


**3)** En Python, es posible almacenar una clase en una variable.

**(0.3 pts) R:** Verdadero.

**4)** Al momento de crear una instancia siempre se llama al `__new__` de la metaclase de su clase.

**(0.1 pts) R:** Falso.

**(0.2 pts) Justificación:** Se llama al `__call__`.

---

### Desarrollo rápido (1.8 pts)

**1) (0.8 pts)** Nombre los parámetros necesarios para definir una clase en Python.

**R:** Los tres parámetros para definir una clase son: el nombre, las bases y los atributos (i.e. `name`, `bases`, `attrs`).

**Puntajes:**

**(0,2 pts)** Nombra sólo uno.

**(0.5 pts)** Nombra sólo dos.

**(0.8 pts)** Nombra los tres.

**2) (1.0 pts)** Con metaclases, ¿qué se debe modificar para que una clase tenga un máximo de cinco instancias? ¿por qué?

**R:** Para lograr eso, se debe modificar el método `__call__` de la metaclase, ya que ese método es el que se llama cuando creamos una nueva instancia; luego, podemos manejar el largo de instancias creadas.

**Puntajes:**

**(0,4 pts)** Mencionar el método `__call__` de la metaclase.

**(0.6 pts)** Correcta justificación.

---

### Desarrollo (3 pts)

**1) (3 pts)** Escriba el _output_ del siguiente programa.

**Nota:** El output cambia según la forma. Además, en la forma de `bar()` hay un error (literalmente). Nuestras disculpas por eso. En esta pregunta se espera que el alumno logre cumplir con las siguientes competencias:

**Puntajes:**

**(0.5 pts)** Métodos `__new__` e `__init__` se llaman **al definir** `MiClase` (y distinguir que el método `__new__` se llama antes del `__init__`).

**(0.5 pts)** Método `__call__` se llama **al instanciar** `MiClase`.

**(0.5 pts)** Identificar que `MiClase` es instancia de `MiMeta`.

**(0.5 pts)** Identificar que `c` **no** es instancia de `MiMeta`. (o bien el error en la forma de `bar`)

**(0.5 pts)** Identificar qué es lo que llega al `__call__`

**(0.5 pts)** Distinguir que modificaciones al diccionario `attrs` sólo sirve antes del llamado a `super()` en el método `__new__`.

#### Outputs

Se muestran a continuación los _outputs_ de las distintas formas:

- _Output_ de `bar`:

```
new MiClase
init MiClase
NameError: name 'c' is not defined # ó False
call con 1=() 2={'b': [4, 8, 15, 16, 23, 42]}
True
97
```


- _Output_ de `foo`:

```
new MiClase
init MiClase
True
call con 1=() 2={'b': [4, 8, 15, 16, 23, 42]}
False
42
```

- _Output_ de `qux`:

```
new MiClase
init MiClase
True
call con 1=() 2={'b': [4, 8, 15, 16, 23, 42]}
False
97
```
