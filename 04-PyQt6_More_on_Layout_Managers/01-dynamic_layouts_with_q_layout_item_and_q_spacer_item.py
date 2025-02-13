from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QSpacerItem, QLayoutItem, QSizePolicy
from PyQt6.QtGui import QIcon
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 Dynamic Layoults with QLayoutItem and QSpacerItem")
        self.setWindowIcon(QIcon('images/icon.png'))

        vbox = QVBoxLayout()

        label = QLabel("Welcome to MMU")
        vbox.addWidget(label)

        button = QPushButton("Add Spacer")
        button.clicked.connect(self.add_spacer)
        vbox.addWidget(button)

        self.setLayout(vbox)

    def add_spacer(self):
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)   

        layout = self.layout()

        layout.addItem(spacer)





app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())