from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 500, 300)
        self.setWindowTitle("PyQt6 QPushButton")
        self.setWindowIcon(QIcon('../images/icon.png'))

        self.create_button()
        
    def create_button(self):
        btn = QPushButton("Click Me", self)
        btn.setGeometry(10, 10, 120, 50)
        btn.setFont(QFont('Arial', 10, QFont.Weight.Bold))
        btn.setIcon(QIcon('images/icon.png'))
        btn.setIconSize(QSize(30, 30))

        # Pop-up menu
        menu = QMenu()
        menu.setFont(QFont('Arial', 10, QFont.Weight.Bold))
        menu.setStyleSheet('background-color: blue')
        menu.addAction('New')
        menu.addAction('Open')
        menu.addAction('Save')

        btn.setMenu(menu)


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())