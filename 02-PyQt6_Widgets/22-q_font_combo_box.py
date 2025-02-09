from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(459, 488)
        Form.setStyleSheet("background-color: #222222;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setStyleSheet("font-size: 15px;\n"
                                 "color: white;\n"
"font-weight: bold;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.fontComboBox = QtWidgets.QFontComboBox(parent=Form)
        self.fontComboBox.setStyleSheet("QFontComboBox, QFontComboBo:focus {\n"
"border: 1px solid gray;\n"
"padding: 10px;\n"
"font-size: 15px;\n"
"border-radius: 2px;\n"
"color: white;\n"
"}\n"
"")
        self.fontComboBox.setObjectName("fontComboBox")
        self.fontComboBox.currentFontChanged.connect(self.change_font_type)
        self.horizontalLayout.addWidget(self.fontComboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=Form)
        self.plainTextEdit.setStyleSheet("padding: 10px;\n"
                                         "color: white;\n"
"font-size: 15px;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def change_font_type(self):
        font = QtGui.QFont(self.fontComboBox.currentText())
        self.plainTextEdit.setFont(font)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QFontComboBox"))
        self.label.setText(_translate("Form", "Font Type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
