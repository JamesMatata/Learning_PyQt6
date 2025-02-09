from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFontDialog, QDialog


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 351)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=Dialog)
        self.plainTextEdit.setStyleSheet("padding: 10px;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setStyleSheet("padding: 10px;\n"
"font-size: 15px;\n"
"font-weight: bold;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.change_font)
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.plainTextEdit.setFont(font)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QFontDialog"))
        self.pushButton.setText(_translate("Dialog", "Change Font"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
