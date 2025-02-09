from PyQt6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLabel, QInputDialog, QLineEdit, QPushButton
from PyQt6.QtGui import QIcon, QFont
import sys

class window(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 QInputDialog")
        self.setWindowIcon(QIcon('images/icon.png'))

        self.create_dialog()


    def create_dialog(self):
        hbox = QHBoxLayout()

        label  = QLabel("Choose country:")
        label.setFont(QFont("Arial", 13))

        self.line_edit = QLineEdit()
        self.line_edit.setFont(QFont("Arial", 13))

        btn = QPushButton("Choose Country")
        btn.setFont(QFont("Arial", 13))
        # btn.clicked.connect(self.show_dialog)
        # btn.clicked.connect(self.get_text)
        btn.clicked.connect(self.get_int)

        hbox.addWidget(label)
        hbox.addWidget(self.line_edit)
        hbox.addWidget(btn)

        self.setLayout(hbox)

    def show_dialog(self):
        countries = [
            "Nigeria", "Ghana", "Kenya", "South Africa", "Togo", "Benin", "Morocco", "Egypt", "Algeria"
        ]

        country, ok = QInputDialog.getItem(self, "Select Country", "Select Country", countries, 0, False)

        if ok and country:
            self.line_edit.setText(country)

    def get_text(self):
        text, ok = QInputDialog.getText(self, "Get Text", "Enter Country name:")   

        if ok and text:
            self.line_edit.setText(text)

    def get_int(self):
        number, ok = QInputDialog.getInt(self, "Get Number", "Enter a number:")

        if ok and number:
            self.line_edit.setText(str(number))

app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())