from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QColorDialog, QDialog


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(398, 388)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=Dialog)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setStyleSheet("padding: 10px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.choose_color)
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setStyleSheet("padding: 10px;\n"
"font-size: 15px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.label.setText(f"Color: {color.name()}")
            self.label.setStyleSheet(f"font-weight: bold;color: {color.name()}")
            self.plainTextEdit.setStyleSheet(f"color: {color.name()}")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QColorDialog"))
        self.pushButton.setText(_translate("Dialog", "Change Color"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
