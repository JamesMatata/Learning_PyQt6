from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QComboBox
from PyQt6.QtGui import QIcon, QPainter, QFont, QColor
from PyQt6.QtCore import Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 600, 350)
        self.setWindowTitle("PyQt6 Drawing Text by Click")
        self.setWindowIcon(QIcon('images/icon.png'))

        self.text = ""
        self.font_size = 12

        vbox = QVBoxLayout()

        self.text_input = QTextEdit()
        self.text_input.setMaximumHeight(150)

        self.combo = QComboBox()
        self.combo.addItems(["12", "14", "16", "18", "20", "22", "24", "26", "28", "30"])
        self.combo.setFont(QFont("Arial", 14))

        button = QPushButton("Draw Text")
        button.setFont(QFont("Arial", 14))
        button.clicked.connect(self.draw_text)

        vbox.addWidget(self.text_input)
        vbox.addWidget(self.combo)
        vbox.addWidget(button)

        self.setLayout(vbox)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(QColor(168, 30, 3))
        painter.setFont(QFont("Arial", self.font_size))

        painter.drawText(event.rect(), Qt.AlignmentFlag.AlignTop, self.text)

        painter.end()

    def draw_text(self):
        self.text = self.text_input.toPlainText()
        self.font_size = int(self.combo.currentText())
        self.update()
        

app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())