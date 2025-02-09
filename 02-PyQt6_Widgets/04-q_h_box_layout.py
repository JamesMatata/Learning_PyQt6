from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QHBoxLayout")
        self.setWindowIcon(QIcon('images/icon.png'))

        # Horizontal Box Layout is used to arrange widgets horizontally
        hbox = QHBoxLayout()

        btn1 = QPushButton("Button 1")
        btn2 = QPushButton("Button 2")
        btn3 = QPushButton("Button 3")
        btn4 = QPushButton("Button 4")

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)

        hbox.addSpacing(50)

        self.setLayout(hbox)



app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())