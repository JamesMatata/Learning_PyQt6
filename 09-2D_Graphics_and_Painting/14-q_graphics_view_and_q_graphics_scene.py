from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene, QGraphicsItem
from PyQt6.QtGui import QIcon, QPen, QBrush
from PyQt6.QtCore import Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 QGraphicView and QGraphicsScene")
        self.setWindowIcon(QIcon('images/icon.png'))

        scene = QGraphicsScene()

        green_brush = QBrush(Qt.GlobalColor.green)
        blue_brush = QBrush(Qt.GlobalColor.blue)

        red_pen = QPen(Qt.GlobalColor.red, 3)
        pink_pen = QPen(Qt.GlobalColor.magenta, 3)

        ellipse = scene.addEllipse(100,100,200,200, red_pen, green_brush)
        rect = scene.addRect(-100,-100,200,200, pink_pen, blue_brush)

        # To make the items movable
        ellipse.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)    

        view = QGraphicsView(scene, self)
        view.setGeometry(0,0,400,250)


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())