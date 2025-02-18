from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPainter, QPen
from PyQt6.QtCore import Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 Drawing a Point with Click")
        self.setWindowIcon(QIcon('images/icon.png'))

        self.pos1 = [0,0]

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)

        pen = QPen(Qt.GlobalColor.red, 15)
        painter.setPen(pen)
        painter.drawPoint(self.pos1[0], self.pos1[1])

        painter.end()

    def mousePressEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.pos1[0], self.pos1[1] = self.pos().x(), self.pos().y()
            self.update()




app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())