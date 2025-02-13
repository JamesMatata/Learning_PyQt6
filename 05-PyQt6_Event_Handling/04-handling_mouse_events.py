from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon, QPainter, QPen
from PyQt6.QtCore import Qt, QEvent
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 Handling Mouse Events")
        self.setWindowIcon(QIcon('images/icon.png'))

        self.start_pos = None
        self.end_pos = None

    def mousePressEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.start_pos = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.end_pos = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.end_pos = event.pos()
            self.update()

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            print("Double Clicked at", event.pos())

    def wheelEvent(self, event):
        angle = event.angleDelta().y()
        if angle > 0:
            print("Wheel Up", angle)
        else:
            print("Wheel Down", angle)

    def paintEvent(self, event):
        if self.start_pos and self.end_pos:
            painter = QPainter(self)
            pen = QPen()
            pen.setWidth(2)
            pen.setColor(Qt.GlobalColor.red)
            painter.setPen(pen)
            painter.drawLine(self.start_pos, self.end_pos)


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())