from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTime, QTimer
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 250)
        self.setWindowTitle("PyQt6 QLCDNumber")
        self.setWindowIcon(QIcon('images/icon.png'))

        # Create a QVBoxLayout
        self.layout = QVBoxLayout()

        # Create the LCD widget
        self.lcd = QLCDNumber(8)  # Ensure enough space for hours, minutes, and seconds
        self.lcd.setStyleSheet("background-color: black; color: white;")
        self.layout.addWidget(self.lcd)

        self.setLayout(self.layout)

        # Timer setup
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateLCD)
        self.timer.start(1000)

        # Show the initial time
        self.updateLCD()

    def updateLCD(self):
        # Update the time on the LCD
        time = QTime.currentTime()
        text = time.toString('hh:mm:ss')  # Include seconds, with two digits for the hour
        self.lcd.display(text)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
