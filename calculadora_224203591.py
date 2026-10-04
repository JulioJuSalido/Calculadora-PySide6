import sys
from PySide6.QtWidgets import (QApplication, QWidget, QFormLayout, QVBoxLayout,  QLabel, QLineEdit, QPushButton, QMessageBox)
# Julio César Ju Salido

class VentanaCalculadora(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora - Julio Cesar Ju Salido ")

        self.Pcalculadora = QFormLayout()

        self.calculadora_label = QLabel("Ingrese la operacion:")
        self.Pcalculadora.addRow(self.calculadora_label)
        self.calculadora_input = QLineEdit()
        self.Pcalculadora.addRow(self.calculadora_input)

        self.operacion_btn = QPushButton("Realizar operacion")
        self.Pcalculadora.addRow(self.operacion_btn)
        self.operacion_btn.clicked.connect(self.operacion)

        self.instrucciones = QLabel("Instrucciones de uso:")
        self.instruccioness = QLabel("Utilice; Suma: + , Resta: -, Multiplicacion: x, Division: /")
        self.instruccionesssss = QLabel("Solo se permiten numeros enteros")
        self.instruccionesss = QLabel("Solo se permiten operaciones con dos numeros")
        self.instruccionessss = QLabel("No utilice espacios")
        self.Pcalculadora.addRow(self.instrucciones)
        self.Pcalculadora.addRow(self.instruccioness)
        self.Pcalculadora.addRow(self.instruccionesssss)
        self.Pcalculadora.addRow(self.instruccionesss)
        self.Pcalculadora.addRow(self.instruccionessss)

        self.setLayout(self.Pcalculadora)

    def operacion(self):
        numero1 = []
        numero2 = []
        datos = self.calculadora_input.text().strip().lower()
        lista = list(datos)
        n = 0
        if " " in datos:
            QMessageBox.warning(self, "Error:", " No utilice espacios")
            return
        for x in lista:
            if x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '0':
                numero1.append(x)
                n += 1
                continue
            elif lista[0] != '1' and lista[0] != '2' and lista[0] != '3' and lista[0] != '4' and lista[0] != '5' and lista[0] != '6' and lista[0] != '7' and lista[0] != '8' and lista[0] != '9' and lista[0] != '0':
                QMessageBox.warning(self, "Error:", " La operacion no puede tener numeros negativos o simbolos antes del numero")
                return
            else:
                break
        if n == 0:
            QMessageBox.warning(self, "Error:", " Su operacion no tiene el primer numero")
            return
        if n >= len(lista):
            QMessageBox.warning(self, "Error:", " Su operacion le hace falta operador y segundo numero")
            return
        if lista[n] != '+' and lista[n] != '-' and lista[n] != 'x' and lista[n] != '/':
            QMessageBox.warning(self, "Error:", " Operador invalido")
            return
        if n + 1 >= len(lista):
            QMessageBox.warning(self, "Error:", " La operacion esta incompleta")
            return
        if lista[n + 1] == '+' or lista[n + 1] == '-' or lista[n + 1] == 'x' or lista[n + 1] == '/':
            QMessageBox.warning(self, "Error:", " Caracter invalido al lado derecho del operador")
            return
        operador = lista[n]
        h = 0
        for x in range(n + 1, len(lista)):
            if lista[x] == '1' or lista[x] == '2' or lista[x] == '3' or lista[x] == '4' or lista[x] == '5' or lista[x] == '6' or lista[x] == '7' or lista[x] == '8' or lista[x] == '9' or lista[x] == '0':
                numero2.append(lista[x])
                h += 1
                continue
            else:
                QMessageBox.warning(self, "Error:", " El segundo numero no es valido, contiene caracteres que no son digitos")
                return
        if h == 0:
            QMessageBox.warning(self, "Error:", " Su operacion no tiene el segundo numero")
            return
        try:
            uno = 0
            dos = 0
            resultado = 0
            for x in numero1:
                uno = uno * 10 + int(x)
            for x in numero2:
                dos = dos * 10 + int(x)

            if operador == '+':
                resultado = uno + dos
            elif operador == '-':
                resultado = uno - dos
            elif operador == 'x':
                resultado = uno * dos
            elif operador == '/':
                if dos == 0:
                    raise ZeroDivisionError
                resultado = uno / dos

        except ZeroDivisionError:
            QMessageBox.warning(self, "Error:", " No se puede dividir entre cero")
            return
        else:
            QMessageBox.information(self, "Resultado:", f" {uno} {operador} {dos} = {resultado}")

if __name__ == "__main__":
    # Inicialización de la aplicación.
    app = QApplication(sys.argv)

    # Crear la ventana
    ventana = VentanaCalculadora()
    ventana.show()
    # Ciclo de eventos de la aplicación.
    sys.exit(app.exec())