from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 Event Handling")
        self.setWindowIcon(QIcon('images/icon.png'))

        self.create_widget()

    def create_widget(self):
        hbox = QHBoxLayout()
        btn = QPushButton("Change Text")

        btn.clicked.connect(self.clicked_btn)

        self.label = QLabel("Hello World")

        hbox.addWidget(btn)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def clicked_btn(self):
        self.label.setText("Button Clicked")
        self.label.setFont(QFont("Times", 20))
        self.label.setStyleSheet("color: red")


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())