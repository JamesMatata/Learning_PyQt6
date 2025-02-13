from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QFormLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 QFormLayout")
        self.setWindowIcon(QIcon('images/icon.png'))

        main_layout = QVBoxLayout()

        form_layout = QFormLayout()

        label1 = QLabel("First Name:")
        line1 = QLineEdit()

        label2 = QLabel("Last Name:")
        line2 = QLineEdit()

        label3 = QLabel("Email:")
        line3 = QLineEdit()

        button = QPushButton("Submit")

        form_layout.addRow(label1, line1)
        form_layout.addRow(label2, line2)
        form_layout.addRow(label3, line3)
        form_layout.addRow(button)

        main_layout.addLayout(form_layout)

        self.setLayout(main_layout)


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())