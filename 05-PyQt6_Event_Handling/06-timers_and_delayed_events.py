from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QTimer, Qt, QElapsedTimer
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 Timers and Delay Events")
        self.setWindowIcon(QIcon('images/icon.png'))

        vbox = QVBoxLayout()

        self.label = QLabel("---[]----[]---")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont('Times', 18))
        vbox.addWidget(self.label)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_label)

        self.elapsed_timer = QElapsedTimer()

        self.setLayout(vbox)

    def start_timer(self):
        self.timer.start()
        self.elapsed_timer.start()


    def update_label(self):
        self.label.setText(f"Elapsed Time: {self.elapsed_timer.elapsed() / 1000:.1f} seconds")


app = QApplication(sys.argv)
window = window()
window.show()
window.start_timer()
sys.exit(app.exec())