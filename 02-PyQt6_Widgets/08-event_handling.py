from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(392, 290)
        Form.setStyleSheet("background-color: white;")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 160, 370, 45))
        self.label.setStyleSheet("font-size: 18px;\n"
"font-weight: bold;\n"
"color: blue;\n"
"text-decoration: underline;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 372, 98))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(370, 45))
        self.lineEdit.setStyleSheet("border: 3px solid blue;\n"
"color: blue;\n"
"padding: 5px;\n"
"font-size: 15px;")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QtCore.QSize(370, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: white;\n"
"background-color: blue;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.display_text)
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def display_text(self):
        text = self.lineEdit.text()
        self.label.setText(text)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Text Displayer"))
        self.label.setText(_translate("Form", "---------------"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Type Your Text"))
        self.pushButton.setText(_translate("Form", "Show Text"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
