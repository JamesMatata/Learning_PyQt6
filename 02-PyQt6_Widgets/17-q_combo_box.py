from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 QComboBox")
        self.setWindowIcon(QIcon('images/icon.png'))

        self.create_combo()


    def create_combo(self):
        hbox = QHBoxLayout()

        label = QLabel("Select account type:")
        label.setFont(QFont('Arial', 13))

        self.combo = QComboBox()
        self.combo.addItem("Admin")
        self.combo.addItem("User")
        self.combo.addItem("Guest")
        self.combo.currentTextChanged.connect(self.combo_changed)

        vbox = QVBoxLayout()

        self.label_result = QLabel("Selected: ")
        self.label_result.setFont(QFont('Arial', 13))


        hbox.addWidget(label)
        hbox.addWidget(self.combo)

        vbox.addLayout(hbox)
        vbox.addWidget(self.label_result)

        self.setLayout(vbox)

    def combo_changed(self):
        self.label_result.setText(f"Selected: {self.combo.currentText()}")


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())