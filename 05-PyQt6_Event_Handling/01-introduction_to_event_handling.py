from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 Introduction to Event Handling")
        self.setWindowIcon(QIcon('images/icon.png'))

        vbox = QVBoxLayout()

        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.on_button_click)
        vbox.addWidget(self.button)

        self.label = QLabel("No button clicked yet")
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.installEventFilter(self)

    def on_button_click(self):
        self.label.setText("Button clicked")

    def eventFilter(self, obj, event):
        if obj is self and event.type() == event.Type.KeyPress:
            print("Key pressed", event.key())
            return True
        return super().eventFilter(obj, event)



app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())