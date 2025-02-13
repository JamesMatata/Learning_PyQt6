from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt6.QtGui import QIcon
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 130)
        self.setWindowTitle("PyQt6 Advanced Styling")
        self.setWindowIcon(QIcon('images/icon.png'))

        vbox = QVBoxLayout()

        label = QLabel("Enter your name:")
        vbox.addWidget(label)

        line = QLineEdit()
        vbox.addWidget(line)

        button = QPushButton("Submit")
        vbox.addWidget(button)

        self.setLayout(vbox)

        self.setStyleSheet(
            """
            QWidget {
            background-color: #f0f0f0;
            }
            QLabel {
                font-size: 18px;
                color: blue;
                font-weight: bold;
                margin-bottom: 10px;
            }
            QLineEdit {
                font-size: 16px;
                padding: 10px;
                border: 1px solid blue;
                border-radius: 5px;
            }
            QPushButton {
                background-color: blue;
                color: white;
                font-size: 18px;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
            }
            QPushButton:hover, QPushButton:pressed {
                background-color: darkblue;
            }
            """
        )


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())