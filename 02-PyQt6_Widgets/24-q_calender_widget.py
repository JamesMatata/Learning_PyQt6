from PyQt6.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 500, 300)
        self.setWindowTitle("PyQt6 QCalendarWidget")
        self.setWindowIcon(QIcon('images/icon.png'))

        vbox = QVBoxLayout()

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.calendar_date)

        self.label = QLabel("---[]----[]---")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont('Arial', 15))
        self.label.setStyleSheet("margin-top: 10px;color: green;")

        vbox.addWidget(self.calendar)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def calendar_date(self):
        self.label.setText(f"## {self.calendar.selectedDate().toString('yyyy-MM-dd')} ##")


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())