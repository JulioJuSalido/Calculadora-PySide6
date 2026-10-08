# Calculadora PySide6
Aplicación de escritorio desarrollada en Python utilizando PySide6. El programa permite realizar operaciones básicas entre dos números enteros mediante una interfaz gráfica.

<img width="662" height="500" alt="image" src="https://github.com/user-attachments/assets/62bc2480-bbe3-407b-aece-2a7e30683649" />

## Descripción
La aplicación cuenta con una ventana donde el usuario puede introducir una operación y ejecutarla mediante un botón.

Las operaciones disponibles son:

- Suma (`+`)
- Resta (`-`)
- Multiplicación (`x`)
- División (`/`)

La aplicación también realiza diferentes validaciones para evitar operaciones incorrectas y muestra mensajes de error cuando los datos ingresados no cumplen con las instrucciones.

## Tecnologías utilizadas
  Python
  PySide6
  QWidget
  QFormLayout
  QLabel
  QLineEdit
  QPushButton
  QMessageBox

## Instrucciones de uso

La operación debe escribirse directamente en el campo de texto.

Ejemplos:

```text
25+10
50-20
8x5
100/4
```

## Reglas:

* Solo se permiten **números enteros**.
* Solo se pueden utilizar **dos números** por operación.
* No se deben utilizar espacios.
* La operación debe contener uno de los siguientes operadores:

```text
+
-
x
/
```
