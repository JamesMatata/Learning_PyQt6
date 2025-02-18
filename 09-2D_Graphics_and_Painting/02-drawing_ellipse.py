from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPainter, QPen, QBrush
from PyQt6.QtCore import Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 Drawing Ellipse - QPainter")
        self.setWindowIcon(QIcon('images/icon.png'))


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.darkBlue , 2, Qt.PenStyle.DotLine))
        painter.setBrush(QBrush(Qt.GlobalColor.green, Qt.BrushStyle.SolidPattern))
        painter.drawEllipse(100, 15, 200, 100)


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())