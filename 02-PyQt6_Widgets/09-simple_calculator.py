from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(369, 266)
        Form.setStyleSheet("QWidget {background-color:  white;}\n"
"QLabel {\n"
"color: black;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid black;\n"
"    color: black;\n"
"    font-size: 14px;\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"background-color: black;\n"
"height: 40px;\n"
"width: 40px;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"}\n"
"")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 120, 40))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 120, 40))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 120, 40))
        self.label_3.setObjectName("label_3")
        self.num1 = QtWidgets.QLineEdit(parent=Form)
        self.num1.setEnabled(True)
        self.num1.setGeometry(QtCore.QRect(150, 10, 200, 40))
        self.num1.setObjectName("num1")
        self.num2 = QtWidgets.QLineEdit(parent=Form)
        self.num2.setGeometry(QtCore.QRect(150, 70, 200, 40))
        self.num2.setMinimumSize(QtCore.QSize(45, 0))
        self.num2.setObjectName("num2")
        self.results = QtWidgets.QLineEdit(parent=Form)
        self.results.setGeometry(QtCore.QRect(150, 200, 200, 40))
        self.results.setObjectName("results")
        self.add_button = QtWidgets.QPushButton(parent=Form)
        self.add_button.setGeometry(QtCore.QRect(21, 130, 81, 48))
        self.add_button.setObjectName("add_button")
        self.add_button.clicked.connect(self.add)
        self.substract_button = QtWidgets.QPushButton(parent=Form)
        self.substract_button.setGeometry(QtCore.QRect(108, 130, 75, 48))
        self.substract_button.setObjectName("substract_button")
        self.substract_button.clicked.connect(self.subtract)
        self.divide_button = QtWidgets.QPushButton(parent=Form)
        self.divide_button.setGeometry(QtCore.QRect(189, 130, 75, 48))
        self.divide_button.setObjectName("divide_button")
        self.divide_button.clicked.connect(self.divide)
        self.multiply_button = QtWidgets.QPushButton(parent=Form)
        self.multiply_button.setGeometry(QtCore.QRect(270, 130, 81, 48))
        self.multiply_button.setObjectName("multiply_button")
        self.multiply_button.clicked.connect(self.multiply)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def add(self):
        num1 = int(self.num1.text())
        num2 = int(self.num2.text())
        result = num1 + num2
        self.results.setText(' + :  ' + str(result))

    def subtract(self):
        num1 = int(self.num1.text())
        num2 = int(self.num2.text())
        result = num1 - num2
        self.results.setText(' - :  ' + str(result))

    def divide(self):
        num1 = int(self.num1.text())
        num2 = int(self.num2.text())
        result = num1 / num2
        self.results.setText(' / :  ' + str(result))

    def multiply(self):
        num1 = int(self.num1.text())
        num2 = int(self.num2.text())
        result = num1 * num2
        self.results.setText(' * :  ' + str(result))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Simple Calculator"))
        self.label.setText(_translate("Form", "First Number"))
        self.label_2.setText(_translate("Form", "Second Number"))
        self.label_3.setText(_translate("Form", "Results"))
        self.add_button.setText(_translate("Form", "+"))
        self.substract_button.setText(_translate("Form", "-"))
        self.divide_button.setText(_translate("Form", "/"))
        self.multiply_button.setText(_translate("Form", "*"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
