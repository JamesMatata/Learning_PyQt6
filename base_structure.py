from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 ")
        self.setWindowIcon(QIcon('images/icon.png'))


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())