from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt6.QtGui import QIcon
from my_rect import MyRect
import sys

class window(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.setFixedSize(800,600)   
        self.show()

        scene = QGraphicsScene()

        # Create rect item
        # rect = QGraphicsRectItem()

        rect = MyRect()

        rect.setRect(0,0,100,100)
        scene.addItem(rect)

        # Make the rect focusable
        rect.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsFocusable)
        rect.setFocus()

        self.setScene(scene)


app = QApplication(sys.argv)
window = window()
sys.exit(app.exec())