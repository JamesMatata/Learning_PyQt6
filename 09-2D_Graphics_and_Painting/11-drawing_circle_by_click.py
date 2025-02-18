from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPainter
from PyQt6.QtCore import QRect, Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 Drawing Circle By Click")
        self.setWindowIcon(QIcon('images/icon.png'))

        self.pos1 = [0,0]
        self.pos2 = [0,0]

    def paintEvent(self, event):
        width = self.pos2[0] - self.pos1[0]
        height = self.pos2[1] - self.pos1[1]

        painter = QPainter(self)
        painter.begin(self)

        rect = QRect(self.pos1[0], self.pos1[1], width, height)

        start_angle = 0
        arc_legnth = 360 * 16

        painter.drawArc(rect, start_angle, arc_legnth)

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