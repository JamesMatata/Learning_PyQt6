from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QRadialGradient, QPainter, QBrush, QPen
from PyQt6.QtCore import Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 QRadialGradient")
        self.setWindowIcon(QIcon('images/icon.png'))

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setPen(QPen(Qt.GlobalColor.darkBlue , 4, Qt.PenStyle.SolidLine))

        radio_gradient = QRadialGradient(100, 100, 100)

        radio_gradient.setColorAt(0.0, Qt.GlobalColor.red)
        radio_gradient.setColorAt(0.5, Qt.GlobalColor.green)
        radio_gradient.setColorAt(1.0, Qt.GlobalColor.blue)

        painter.setBrush(QBrush(radio_gradient))

        painter.drawEllipse(10, 10, 200, 200)


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())