# Control 2

### Verdadero o False (2.5 puntos)
Todas las preguntas tienen 0.5 puntos. En el caso de las falsas:
  - Si una pregunta está correcta pero mal justificada serán 0.1 puntos.
  - Si una pregunta está correcta pero con justificación incompleta serán 0.25 puntos.
  - Si una pregunta está correcta y bien justificada se otrogará el puntaje completo.

1. Un layout permite manejar la distribución espacial de los widgets.

      **Respuesta:** Verdadero (0.5 puntos).

2. Si se cambia el nombre del archivo `archivo.png` a `archivo.pdf` se altera el contenido del archivo.

      **Respuesta:** Falso. La extensión es sólo un atajo para que el computador sepa con que programa abirir
      el archivo, por lo que el contenido del archivo no es modificado. (0.5 puntos).

3. El path ‘../carpeta/archivo.pdf’ es de tipo absoluto.

      **Respuesta:** Falso. Un path absoluto parte siempre con '/'. (0.5 puntos).

4. Los objetos del tipo `bytes` y del tipo `bytearray` representan secuencias de bytes.

      **Respuesta:** Verdadero (0.5 puntos).

5. Un objeto del tipo `bytes` tiene el método `extend`.

      **Respuesta:** Falso. Los `bytes` son inmutables. También es válido argumentar que es un método de `bytearray`. (0.5 puntos).

### Desarrollo Rápido (2.0 puntos)

1. Mencione y explique dos ventajas de usar un modelo _Backend / Frontend_

      **Respuesta:** Se consideró correcto la justificación a partir de alguna de las siguientes características descritas en el material: **modularidad, uso de recursos, escalamiento, experticia, mantención, evolución del _software_ / escalamiento**. Por otro lado, el argumento de que es un modelo de bajo acomplamiento y alta cohesión también se consideró correcto siempre y cuando se haya justificado correctamente. (0.5 puntos).

2. Explique qué es el encoding  y por qué ocupar el correcto es importante.

      **Respuesta:** El encoding es una forma de traducir bytes a caracteres. Es importante ya que el uso de un _encoding_ incorrecto podrá recaer en errores o interpretación errónea de caracteres.

### Códigos (2.5 puntos)

1. Escriba el _output_ del siguiente programa:

  **Forma 1:**
  ```python
  mitexto = "Ave César"
  encoded = mitexto.encode("utf-8")
  decoded = encoded.decode("utf-8", errors="ignore")
  print(type(encoded))  # 0.5 puntos
  print(type(decoded))  # 0.5 puntos
  print(decoded)        # 0.5 puntos (bonus)

  # Output
  <class 'bytes'>
  <class 'str'>
  Ave Csar
  ```

  **Forma 2:**
  ```python
  mitexto = "Ave Belén"
  encoded = mitexto.encode("utf-8")
  decoded = encoded.decode("utf-8", errors="ignore")
  print(type(encoded))  # 0.5 puntos
  print(type(decoded))  # 0.5 puntos
  print(decoded)        # 0.5 puntos (bonus)

  # Output
  <class 'bytes'>
  <class 'str'>
  Ave Beln
  ```

  **Forma 3:**
  ```python
  mitexto = "Qué Frío"
  encoded = mitexto.encode("utf-8")
  decoded = encoded.decode("utf-8", errors="ignore")
  print(type(encoded))  # 0.5 puntos
  print(type(decoded))  # 0.5 puntos
  print(decoded)        # 0.5 puntos (bonus)

  # Output
  <class 'bytes'>
  <class 'str'>
  Qu Fro
  ```

2. Escriba el _output_ del siguiente programa:

  **Forma 1:**
  ```python
  data = b"\x6e\x65\x62\x63\x6f\x69\x6e"
  print(len(data))              # 0.5 puntos
  print(data.decode("ascii"))   # 0.5 puntos (bonus)

  # Output
  6
  'nebcoin'
  ```

  **Forma 2:**
  ```python
  data = b"\x63\x75\x61\x74\x72\x6f"
  print(len(data))              # 0.5 puntos
  print(data.decode("ascii"))   # 0.5 puntos (bonus)

  # Output
  6
  'cuatro'
  ```

  **Forma 3:**
  ```python
  data = b"\x63\x69\x6e\x63\x6f"
  print(len(data))              # 0.5 puntos
  print(data.decode("ascii"))   # 0.5 puntos (bonus)

  # Output
  5
  'cinco'
  ```  
