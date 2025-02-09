from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QComboBox
from PyQt6 import uic, QtCore
import sys


class window(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi('Designs/combobox.ui', self)

        self.results = self.findChild(QLabel, 'results')
        self.results.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.combo = self.findChild(QComboBox, 'language')

        self.combo.currentTextChanged.connect(self.on_combo_changed)

    def on_combo_changed(self):
        self.results.setText(f"Selected: {self.combo.currentText()}")

app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())