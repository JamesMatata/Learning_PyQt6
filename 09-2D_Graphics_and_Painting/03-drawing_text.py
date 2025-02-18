from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPainter, QPen, QBrush, QTextDocument
from PyQt6.QtCore import Qt, QRect, QRectF
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 Drawing Text - QPainter")
        self.setWindowIcon(QIcon('images/icon.png'))


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.darkBlue , 2, Qt.PenStyle.DotLine))
        painter.setBrush(QBrush(Qt.GlobalColor.green, Qt.BrushStyle.SolidPattern))
        painter.drawText(100, 15, 'The Graphics')

        rect = QRect(100, 15, 200, 50)
        painter.drawRect(rect)

        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, 'The Graphics')

        document = QTextDocument()

        rect2 = QRectF(0, 0, 250, 250)
        document.setTextWidth(rect2.width())
        document.setHtml('<h1>The Graphics</h1>')
        document.drawContents(painter, rect2)



app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())