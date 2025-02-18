from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QLinearGradient, QPainter, QBrush, QPen
import sys
from PyQt6.QtCore import Qt

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 QLinearGradient")
        self.setWindowIcon(QIcon('images/icon.png'))

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setPen(QPen(Qt.GlobalColor.darkBlue , 4, Qt.PenStyle.SolidLine))

        grad1 = QLinearGradient(10, 10, 250, 100)

        grad1.setColorAt(0.0, Qt.GlobalColor.red)
        grad1.setColorAt(0.5, Qt.GlobalColor.green)
        grad1.setColorAt(1.0, Qt.GlobalColor.blue)

        painter.setBrush(QBrush(grad1))

        painter.drawRect(10, 10, 250, 100)


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())