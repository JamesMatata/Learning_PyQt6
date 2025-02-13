from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 ")
        self.setWindowIcon(QIcon('images/icon.png'))

        vbox = QVBoxLayout()

        label1 = QLabel("Stretchable Lable")
        label2 = QLabel("Non-Stretchable Lable")

        vbox.addWidget(label1)
        vbox.addWidget(label2)

        vbox.setStretch(0, 1)
        vbox.setStretch(1, 0)


        self.setLayout(vbox)


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())