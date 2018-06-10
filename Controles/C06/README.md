# Control 6

### Los controles son iguales
###### (Sólo varía en el orden de las preguntas)

**(3 pts.) Verdadero o Falso**

> - La simulación síncrona es más eficiente en cuanto a tiempo de ejecución que la simulación por eventos discretos.

**Respuesta**: **Falso**.

**Explicación**: Está en el material, se puede argumentar que en la síncrona se iterarán momentos en donde no ocurre absolutamente nada, mientras que en la simulación por eventos discretos sólo se tomarán en cuenta los momentos donde ocurre algo. Por lo que no habrán _tiempos muertos_ y por ende se vuelve más eficiente.

> - La cola de eventos en DES **solo** permite agregar nuevos eventos con un tiempo de ocurrencia mayor al de **todos** los eventos que ya están en cola.

**Respuesta**: **Falso**

**Explicación**: Dado que es una cola ordenada, el próximo evento puede tener su siguiente ocurrencia después del último evento de la cola o antes de este, por lo que es falso.

> - Los _threads_ se ejecutan de manera secuencial, es decir, uno a continuación de otro.

**Respuesta**: **Falso**

**Explicación**: Más falso imposible, los _threads_ no tienen orden de ejecución y por eso es necesaria la existencia de mecanismos para sincronizarlos (como los ``lock`` o el método ``acquire`` y ``release``)

> - Un programa _multi-threaded_ es más rápido que un programa _single-threaded_

**Respuesta**: **Falso**

**Explicación**: En caso que el computador sólo tenga un _core_, el programa en realidad correrá igual de rápido. Según el contenido _"Cuando hay un sólo procesador, no existe un verdadero aumento de la velocidad de ejecución, pero sí de la manera en que el programa responde. En máquinas con más procesadores, efectivamente se logra la ejecución en paralelo de varios threads, que tiene como resultado una ejecución más rápida del programa."_

> - Un _daemon-thread_ continua ejecutándose independiente de si el programa principal ha terminado.

**Respuesta**: **Falso**

**Explicación**: Este tipo de _threads_ hace justamente lo contrario, estos se acaban junto con el programa principal. Salvo que estes en _jupyter-notebook_ o _IDLE_, pero eso es por otro motivo independiente de los _daemon-threads_.

> - Una vez que un _thread t_ ha ejecutado ``lock.acquire()``, otros _threads_ no pueden continuar más allá de ese punto hasta que el _thread t_ ejecute ``lock.release()``

**Respuesta**: **Verdadero**

**Explicación**: Según el enunciado, los otros _threads_ comparten el código (dado que llegan al "punto" donde se hace ``lock.acquire()``). La idea de los ``lock`` es justamente lograr sincronizar los _threads_ de forma que el resto espere en la misma zona donde se llama el ``lock``. 

---

**(3 Pts.) Desarrollo Rápido**

> (0.75 Pts.) Explique por qué utilizaría simulación de procesos para resolver un problema.

**Explicación:** Obtenido desde el material del curso; la principal razón es que _"los sistemas reales incluyen comportamientos más complejos difíciles de representar usando solo un modelo analítico"_ y que debido a esto, se estiman utilizando modelación.

Otros motivos aceptados son:

- Ver un problema que tiene alta aleatoriedad y que es complejo de analizar.
- Comprender el comportamiento del sistema y evaluar el funcionamiento del modelo a implementar.
- Reducción de costos y riesgos.
- Experimentación rápida del modelo en comparación al uso de sistemas en tiempo real.

Cualquiera de estos será aceptado para tener el puntaje completo

---

> (0.75 Pts.) Explique la diferencia entre tiempo de simulación y tiempo de ejecución.

**Puntaje:** :
- **(0.4 Pts)** Si sólo explicó uno de los dos tiempos
- **(0.75 Pts)** Da diferencias anotando de qué se tratan ambos tiempos.

**Explicación:** Bastaba con explicar que el primero es el tiempo _virtual_ de la simulación, es decir, el tiempo a simular. Mientras que el **tiempo de ejecución** es lo que se demora en llevarse a cabo la simulación en **tiempo real**. Cualquier explicación similar a esta tiene el puntaje completo.

---

> (0.75 Pts.) ¿Qué permite realizar el método ``join`` de la clase ``Thread``?.

**Explicación:** Permite que el sistema que llama al método ``join()`` (puede ser el principal u otro _thread_) de dicho _thread_ espere hasta que este último termine su proceso.

---

> (0.75 Pts.) Mencione dos escentarios donde es beneficioso utilizar _threading_.

**Puntaje:** :

- **(0.4 Pts)** Tener un sólo escenario explicado
- **(0.75 Pts)** Explica dos escenarios bien.

**Explicación:** Como existen múltiples casos de uso de threads, conviene considerar que estos son ideales para separar tareas que pueden desarrollarse de forma más o menos independiente, en especial cuando una de ellas consume más tiempo y hace que otras no sean atendidas hasta que termine. Algunos usos concretos (sacados del material de estudio):

- **Interfaces de rápida respuesta**, donde se necesita interactuar con el usuario mientras se ejecuta algún proceso de cómputo pesado. Por ejemplo, las interfaces gráficas en un computador.

- **Delegación de trabajos** que siguen el **patrón consumidor-productor**, en donde existen procesos que se ejecutan secuencialmente, pero que son independientes entre ellos. Como por ejemplo, un thread que se encargue de poner los frames capturados desde una cámara de video en una cola, y otro thread que procese estos cuadros y los saque de la cola.

- **Aplicaciones multiusuario**, en donde cada thread se encargaría de las peticiones de cada usuario independientemente. Por ejemplo, un servidor de páginas web debe atender a varios clientes a la vez.
