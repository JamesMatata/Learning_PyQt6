from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 Mouse Event in QPainter Class")
        self.setWindowIcon(QIcon('images/icon.png'))
        self.setMouseTracking(True)

        hbox = QHBoxLayout()

        self.label = QLabel("Mouse Track")
        self.label.setFont(QFont("Arial", 15))

        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def mouseMoveEvent(self, event):
        x = self.x()
        y = self.y()
        self.label.setText(f"Mouse Coordinates: ({x}, {y})")
        self.update()



app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())