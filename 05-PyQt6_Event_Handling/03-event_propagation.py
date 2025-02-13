from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 Event Propagation")
        self.setWindowIcon(QIcon('images/icon.png'))

        vbox = QVBoxLayout()

        self.parent_button = QPushButton("Parent Button")
        self.parent_button.clicked.connect(self.parent_button_clicked)
        vbox.addWidget(self.parent_button)

        self.child_button = QPushButton("Child Button")
        self.child_button.clicked.connect(self.child_button_clicked)
        vbox.addWidget(self.child_button)

        self.setLayout(vbox)

    def parent_button_clicked(self):
        print("Parent button clicked")
        self.parent_button.setStyleSheet("background-color: green")

    def child_button_clicked(self):
        print("Child button clicked")
        self.child_button.setStyleSheet("background-color: red")

        self.parent_button_clicked()



app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())