from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 131)
        Dialog.setStyleSheet("QPushButton {\n"
"font-size: 15px;\n"
"padding: 10px;\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.warn_msg)
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.info_msg)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.about_msg)
        self.horizontalLayout.addWidget(self.pushButton_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def warn_msg(self):
        msg = QtWidgets.QMessageBox.warning(self, "Warning", "This is a warning message!")

    def info_msg(self):
        msg = QtWidgets.QMessageBox.information(self, "Information", "This is an information message!")

    def about_msg(self):
        msg = QtWidgets.QMessageBox.about(self, "About", "This is an about message!")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QMessageBox"))
        self.pushButton.setText(_translate("Dialog", "Warning"))
        self.pushButton_2.setText(_translate("Dialog", "Information"))
        self.pushButton_3.setText(_translate("Dialog", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
