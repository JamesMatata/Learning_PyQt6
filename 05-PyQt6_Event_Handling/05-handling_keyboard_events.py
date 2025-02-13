from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 Handling Keyboard Events")
        self.setWindowIcon(QIcon('images/icon.png'))

        self.label = QLabel("Press any key", self)
        self.label.setFont(QFont('Times', 18))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)

        self.label.move(100,100)

    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key.Key_Up:
            self.label.move(self.label.x(), self.label.y() - 10)

        elif key == Qt.Key.Key_Down:
            self.label.move(self.label.x(), self.label.y() + 10)
        elif key == Qt.Key.Key_Left:
            self.label.move(self.label.x() - 10, self.label.y())
        elif key == Qt.Key.Key_Right:
            self.label.move(self.label.x() + 10, self.label.y())
        elif key == Qt.Key.Key_Escape:
            self.close()
    
    def keyReleaseEvent(self, event):
        text = event.text()
        print("Key Released: ", text)


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())