from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 296)
        Dialog.setStyleSheet("QDialog {\n"
"background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: blue;\n"
"color: white;\n"
"font-size: 14px;\n"
"padding: 7px;\n"
"border: none;\n"
"border-radius: 3px;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setStyleSheet("color: black;\n"
"font-weight: bold;\n"
"margin-bottom: 10px;\n"
"font-size: 16px;\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(parent=Dialog)
        self.listWidget.setStyleSheet("background-color: white;\n"
"border: 1px solid black;\n"
"padding: 5px;\n"
"border-radius: 3px;\n"
"font-size: 15px;")
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_button = QtWidgets.QPushButton(parent=Dialog)
        self.add_button.setObjectName("add_button")
        self.add_button.clicked.connect(self.add_item)
        self.verticalLayout.addWidget(self.add_button)
        self.edit_button = QtWidgets.QPushButton(parent=Dialog)
        self.edit_button.setObjectName("edit_button")
        self.edit_button.clicked.connect(self.edit_item)
        self.verticalLayout.addWidget(self.edit_button)
        self.remove_button = QtWidgets.QPushButton(parent=Dialog)
        self.remove_button.setObjectName("remove_button")
        self.remove_button.clicked.connect(self.remove_item)
        self.verticalLayout.addWidget(self.remove_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.sort_button = QtWidgets.QPushButton(parent=Dialog)
        self.sort_button.setObjectName("sort_button")
        self.sort_button.clicked.connect(self.sort_items)
        self.verticalLayout.addWidget(self.sort_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def add_item(self):
        row = self.listWidget.currentRow()
        title = "Add Item"
        item, ok = QtWidgets.QInputDialog.getText(self, title, "Enter item name")

        if ok and item:
            self.listWidget.insertItem(row, item)

    def edit_item(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        if item:
            title = "Edit Item"
            text, ok = QtWidgets.QInputDialog.getText(self, title, "Edit item name", text=item.text())
            if ok and text:
                item.setText(text)

    def remove_item(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        if item:
            reply = QtWidgets.QMessageBox.question(self, "Remove Item", "Do you want to remove this item?", QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                item = self.listWidget.takeItem(row)
                del item

    def sort_items(self):
        self.listWidget.sortItems()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Shopping List"))
        self.add_button.setText(_translate("Dialog", "Add"))
        self.edit_button.setText(_translate("Dialog", "Edit"))
        self.remove_button.setText(_translate("Dialog", "Remove"))
        self.sort_button.setText(_translate("Dialog", "Sort"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
