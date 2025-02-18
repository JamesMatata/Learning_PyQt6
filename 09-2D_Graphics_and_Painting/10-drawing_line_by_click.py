from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPainter, QPen
from PyQt6.QtCore import Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 Drawing Line by Click")
        self.setWindowIcon(QIcon('images/icon.png'))

        self.pos1 = [0,0]
        self.pos2 = [0,0]

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)

        pen = QPen(Qt.GlobalColor.blue, 3)
        painter.setPen(pen)

        painter.drawLine(self.pos1[0], self.pos1[1], self.pos2[0], self.pos2[1])
        painter.end()

    def mousePressEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.pos1[0], self.pos1[1] = event.pos().x(), event.pos().y()

    def mouseReleaseEvent(self, event):
        self.pos2[0], self.pos2[1] = event.pos().x(), event.pos().y()
        self.update()


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())