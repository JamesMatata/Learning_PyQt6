from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QConicalGradient, QPainter, QBrush, QPen
from PyQt6.QtCore import Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 QConicalGradient")
        self.setWindowIcon(QIcon('images/icon.png'))

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setPen(QPen(Qt.GlobalColor.darkBlue , 4, Qt.PenStyle.SolidLine))

        conical_gradient = QConicalGradient(100, 100, 10)

        conical_gradient.setColorAt(0.0, Qt.GlobalColor.red)
        conical_gradient.setColorAt(0.5, Qt.GlobalColor.green)
        conical_gradient.setColorAt(1.0, Qt.GlobalColor.blue)

        painter.setBrush(QBrush(conical_gradient))

        painter.drawEllipse(10, 10, 200, 200)


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())