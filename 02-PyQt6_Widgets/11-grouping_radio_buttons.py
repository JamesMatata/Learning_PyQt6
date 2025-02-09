from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 336)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(9, 138, 162, 16))
        self.label_2.setObjectName("label_2")
        self.results = QtWidgets.QLabel(parent=Form)
        self.results.setGeometry(QtCore.QRect(10, 290, 381, 41))
        self.results.setStyleSheet("padding: 10px;\n"
"font-size: 16px;\n"
"font-weight: bold;")
        self.results.setText("")
        self.results.setObjectName("results")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(9, 9, 248, 98))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Beef = QtWidgets.QRadioButton(parent=self.widget)
        self.Beef.setObjectName("Beef")
        self.Beef.toggled.connect(self.radio_selected)
        self.verticalLayout.addWidget(self.Beef)
        self.Chicken = QtWidgets.QRadioButton(parent=self.widget)
        self.Chicken.setObjectName("Chicken")
        self.Chicken.toggled.connect(self.radio_selected)
        self.verticalLayout.addWidget(self.Chicken)
        self.Pork = QtWidgets.QRadioButton(parent=self.widget)
        self.Pork.setObjectName("Pork")
        self.Pork.toggled.connect(self.radio_selected)
        self.verticalLayout.addWidget(self.Pork)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.widget1 = QtWidgets.QWidget(parent=Form)
        self.widget1.setGeometry(QtCore.QRect(9, 160, 84, 100))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.roasting = QtWidgets.QRadioButton(parent=self.widget1)
        self.roasting.setObjectName("roasting")
        self.roasting.toggled.connect(self.radio_selected)
        self.verticalLayout_3.addWidget(self.roasting)
        self.grilling = QtWidgets.QRadioButton(parent=self.widget1)
        self.grilling.setObjectName("grilling")
        self.grilling.toggled.connect(self.radio_selected)
        self.verticalLayout_3.addWidget(self.grilling)
        self.broiling = QtWidgets.QRadioButton(parent=self.widget1)
        self.broiling.setObjectName("broiling")
        self.broiling.toggled.connect(self.radio_selected)
        self.verticalLayout_3.addWidget(self.broiling)
        self.panfrying = QtWidgets.QRadioButton(parent=self.widget1)
        self.panfrying.setObjectName("panfrying")
        self.panfrying.toggled.connect(self.radio_selected)
        self.verticalLayout_3.addWidget(self.panfrying)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def radio_selected(self):
        selected1 = ""
        selected2 = ""

        if self.Beef.isChecked():
            selected1 = self.Beef.text()
        if self.Chicken.isChecked():
            selected1 = self.Chicken.text()
        if self.Pork.isChecked():
            selected1 = self.Pork.text()
        
        if self.roasting.isChecked():
            selected2 = self.roasting.text()
        if self.grilling.isChecked():
            selected2 = self.grilling.text()
        if self.broiling.isChecked():
            selected2 = self.broiling.text()
        if self.panfrying.isChecked():
            selected2 = self.panfrying.text()

        if selected1 and selected2:
            self.results.setText(f"You ordered {selected2} {selected1}!")



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Grouping Radio Buttons"))
        self.label_2.setText(_translate("Form", "How would you like it cooked?"))
        self.label.setText(_translate("Form", "Select the type of meat you would like to order"))
        self.Beef.setText(_translate("Form", "Beef"))
        self.Chicken.setText(_translate("Form", "Chicken"))
        self.Pork.setText(_translate("Form", "Pork"))
        self.roasting.setText(_translate("Form", "roasting"))
        self.grilling.setText(_translate("Form", "grilling"))
        self.broiling.setText(_translate("Form", "broiling"))
        self.panfrying.setText(_translate("Form", "pan-frying"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
