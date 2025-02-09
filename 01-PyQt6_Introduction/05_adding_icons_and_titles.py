from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("My PyQt6 Window")
        # Add an icon to the window
        self.setWindowIcon(QIcon('images/icon.png'))
        # Setting fixed window size
        # self.setFixedWidth(700)
        # self.setFixedHeight(400)

        # Styling the window
        self.setStyleSheet('background-color: lightblue;')

        # Making the window transparent
        self.setWindowOpacity(0.8)

        

app = QApplication(sys.argv)

window = window()

window.show()

sys.exit(app.exec())