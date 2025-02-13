from PyQt6.QtWidgets import QApplication, QWidget, QSplitter, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 QSplitter")
        self.setWindowIcon(QIcon('images/icon.png'))

        main_layout = QVBoxLayout()

        splitter = QSplitter()

        edit1 = QTextEdit()
        edit2 = QTextEdit()

        splitter.addWidget(edit1)
        splitter.addWidget(edit2)

        splitter.setSizes([200, 200])

        main_layout.addWidget(splitter)

        self.setLayout(main_layout)


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())