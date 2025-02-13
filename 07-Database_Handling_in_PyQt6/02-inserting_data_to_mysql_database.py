from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFrame, QWidget
from PyQt6.QtCore import Qt
import mysql.connector as mc


class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 515)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(350, 515))
        Form.setStyleSheet("QWidget {\n"
"background-color: white;\n"
"padding: 5px;\n"
"}\n"
"QLineEdit {\n"
"color: black;\n"
"    font-size: 14px;\n"
"    border: 1px solid blue;\n"
"    padding: 5px;\n"
"    height: 30px;\n"
"border-radius: 2px;\n"
"}\n"
"QPushButton {\n"
"padding: 10px;\n"
"color: white;\n"
"background-color: darkblue;\n"
"font-size: 15px;\n"
"font-weight: bold;\n"
"border: none;\n"
"border-radius: 4px;\n"
"}")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setStyleSheet("color: blue;\n"
"font-size: 30px;\n"
"font-weight: bold;\n"
"")
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_6.addWidget(self.label)
        self.line = QFrame()
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_6.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setStyleSheet("color: black;\n"
"font-size: 15px;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.full_name = QtWidgets.QLineEdit(parent=Form)
        self.full_name.setStyleSheet("")
        self.full_name.setObjectName("full_name")
        self.verticalLayout.addWidget(self.full_name)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setStyleSheet("color: black;\n"
"font-size: 15px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.email = QtWidgets.QLineEdit(parent=Form)
        self.email.setStyleSheet("")
        self.email.setObjectName("email")
        self.verticalLayout_2.addWidget(self.email)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setStyleSheet("color: black;\n"
"font-size: 15px;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.pass1 = QtWidgets.QLineEdit(parent=Form)
        self.pass1.setStyleSheet("")
        self.pass1.setObjectName("pass1")
        self.verticalLayout_4.addWidget(self.pass1)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setStyleSheet("color: black;\n"
"font-size: 15px;")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.pass2 = QtWidgets.QLineEdit(parent=Form)
        self.pass2.setStyleSheet("")
        self.pass2.setObjectName("pass2")
        self.verticalLayout_5.addWidget(self.pass2)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_user)
        self.verticalLayout_6.addWidget(self.pushButton)
        self.result = QtWidgets.QLabel(parent=Form)
        self.result.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.result.setStyleSheet("font-size: 18px;\n"
"font-weight: bold;\n"
"color: black;\n"
"margin-top: 10px;\n"
"\n"
"")
        self.result.setObjectName("result")
        self.verticalLayout_6.addWidget(self.result)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def add_user(self):
        full_name = self.full_name.text()
        email = self.email.text()
        pass1 = self.pass1.text()
        pass2 = self.pass2.text()

        if pass1 == pass2:
            self.result.setText("Passwords Matched")
        else:
            self.result.setText("Passwords do not match")

        try:
            conn = mc.connect(
                host="localhost",
                user="root",
                password="jamesMATATA",
                database="mydatabase"
            )
            if conn.is_connected:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (full_name, email, password) VALUES (%s, %s, %s)", (full_name, email, pass1))
                conn.commit()
                self.result.setText("User added successfully")
                cursor.close()
                conn.close()
        except mc.Error as err:
            self.result.setText(f"Error: {err}")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SignUp"))
        self.label.setText(_translate("Form", "SignUp"))
        self.label_2.setText(_translate("Form", "Full Name:"))
        self.label_3.setText(_translate("Form", "Email:"))
        self.label_5.setText(_translate("Form", "Create Password:"))
        self.label_6.setText(_translate("Form", "Confirm Password:"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.result.setText(_translate("Form", "---[]-----[]---"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
