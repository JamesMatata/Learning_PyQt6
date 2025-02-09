from PyQt6 import QtCore, QtGui, QtWidgets
from random import randint


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 200)
        Form.setStyleSheet("QWidget {\n"
"background-color: #C4A484;}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcdNumber = QtWidgets.QLCDNumber(parent=Form)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.lcdNumber)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setStyleSheet("color: white;\n"
"padding: 15px;\n"
"border-radius: 3px;\n"
"background-color: brown;\n"
"border: none;\n"
"font-weight: bold;\n"
"font-size: 14px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.generate_random_number)
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def generate_random_number(self):
        self.lcdNumber.display(randint(1, 999))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Random Int Generator"))
        self.pushButton.setText(_translate("Form", "Generate Random Number"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
