from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 Mouse Press and Mouse Release Event")
        self.setWindowIcon(QIcon('images/icon.png'))

        self.setMouseTracking(True)

        vbox = QVBoxLayout()

        self.label_press = QLabel("Mouse Press")
        self.label_press.setFont(QFont("Arial", 15)) 

        self.label_release = QLabel("Mouse Release")
        self.label_release.setFont(QFont("Arial", 15))

        vbox.addWidget(self.label_press)
        vbox.addWidget(self.label_release)


        self.setLayout(vbox)

    def mousePressEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            x = self.x()
            y = self.y()
            self.label_press.setText(f"Mouse Pressed: ({x}, {y})")
            

    def mouseReleaseEvent(self, event):
        x = self.x()
        y = self.y()
        self.label_release.setText(f"Mouse Released: ({x}, {y})")
        self.update()


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())