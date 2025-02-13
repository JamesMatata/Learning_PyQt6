from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QDrag
from PyQt6.QtCore import Qt, QMimeData
import sys

class DraggableLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime_data = QMimeData()
            mime_data.setText(self.text())
            drag.setMimeData(mime_data)
            drag.exec(Qt.DropAction.MoveAction)


class DroppableLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        self.setText(event.mimeData().text())
        event.acceptProposedAction()
        

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 Drag & Drop")
        self.setWindowIcon(QIcon('images/icon.png'))

        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout()
        draggable_label = DraggableLabel("Drag me")
        droppable_label = DroppableLabel()

        vbox.addWidget(draggable_label)
        vbox.addWidget(droppable_label)

        self.setLayout(vbox)





app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())