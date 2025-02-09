from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QIcon, QFont
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QLineEdit")
        self.setWindowIcon(QIcon('images/icon.png'))

        line_edit = QLineEdit(self)
        line_edit.setFont(QFont('Arial', 10, QFont.Weight.Bold))
        # Setting default text
        # line_edit.setText("Enter your name") 
        # Setting placeholder text
        #line_edit.setPlaceholderText("Enter your name...")
        # To disable the line edit
        #line_edit.setEnabled(False)
        # To set an Echo Mode
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)




app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())