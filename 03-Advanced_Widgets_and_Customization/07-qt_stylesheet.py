from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QIcon
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 Stylesheet")
        self.setWindowIcon(QIcon('images/icon.png'))

        button = QPushButton("Click Me", self)
        button.setStyleSheet(
            """
                QPushButton {
                    background-color: blue;
                    color: white;
                    font-size: 18px;
                    border: none;
                    border-radius: 5px;
                    padding: 10px 20px;
                }
                QPushButton:hover {
                    background-color: red;
                }
                QPushButton:pressed {
                    background-color: green;
                }
            """
        )
        
        vbox = QVBoxLayout()
        vbox.addWidget(button)

        self.setLayout(vbox)


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())