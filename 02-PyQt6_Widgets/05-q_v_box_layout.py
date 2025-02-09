from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QHBoxLayout")
        self.setWindowIcon(QIcon('images/icon.png'))

        # Horizontal Box Layout is used to arrange widgets horizontally
        vbox = QVBoxLayout()

        btn1 = QPushButton("Button 1")
        btn2 = QPushButton("Button 2")
        btn3 = QPushButton("Button 3")
        btn4 = QPushButton("Button 4")

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        vbox.addSpacing(50)

        self.setLayout(vbox)



app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())