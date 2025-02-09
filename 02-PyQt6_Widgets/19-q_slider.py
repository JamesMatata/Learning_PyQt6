from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 150)
        self.setWindowTitle("PyQt6 QSlider")
        self.setWindowIcon(QIcon('images/icon.png'))

        vbox = QVBoxLayout()

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(5)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.slider_changed)


        self.label = QLabel("---[]----[]---")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont('Arial', 15))

        vbox.addWidget(self.slider)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def slider_changed(self):
        self.label.setText(f"{self.slider.value()}%")


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())