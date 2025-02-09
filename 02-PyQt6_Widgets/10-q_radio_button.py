from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QRadioButton
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize, Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle("PyQt6 QRadioButton")
        self.setWindowIcon(QIcon('images/icon.png'))

        self.creat_radio()

    def creat_radio(self):
        hbox = QHBoxLayout()

        rad1 = QRadioButton('Python')
        rad1.setIcon(QIcon('C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs/Learning_GUIs_with_PyQt6/02-PyQt6_Widgets/images/py.png'))
        rad1.setIconSize(QSize(25,25))
        rad1.setFont(QFont('Arial', 15))
        rad1.toggled.connect(lambda: self.radio_selected('print("*  O O  *")', 'orange'))

        rad2 = QRadioButton('Java')
        rad2.setIcon(QIcon('C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs/Learning_GUIs_with_PyQt6/02-PyQt6_Widgets/images/java.png'))
        rad2.setIconSize(QSize(25,25))
        rad2.setFont(QFont('Arial', 15))
        rad2.toggled.connect(lambda: self.radio_selected('System.out.println("*  O O  *");', 'green'))

        rad3 = QRadioButton('JavaScript')
        rad3.setIcon(QIcon('C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs/Learning_GUIs_with_PyQt6/02-PyQt6_Widgets/images/js.png'))
        rad3.setIconSize(QSize(25,25))
        rad3.setFont(QFont('Arial', 15))
        rad3.toggled.connect(lambda: self.radio_selected('console.log("*  O O  *");', 'red'))

        rad4 = QRadioButton('C++')
        rad4.setIcon(QIcon('C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs/Learning_GUIs_with_PyQt6/02-PyQt6_Widgets/images/cplusplus.png'))
        rad4.setIconSize(QSize(25,25))
        rad4.setFont(QFont('Arial', 15))
        rad4.toggled.connect(lambda: self.radio_selected('cout << "*  O O  *" << endl;', 'blue'))

        hbox.addWidget(rad1)
        hbox.addWidget(rad2)
        hbox.addWidget(rad3)
        hbox.addWidget(rad4)

        self.label = QLabel('---(-)-----======----(-)---')
        self.label.setFont(QFont('Times Roman', 15))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def radio_selected(self, text, color):
        rad = self.sender()
        if rad.isChecked():
            self.label.setText(text)
            self.label.setStyleSheet(f'color: {color};font-weight: bold;')

app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())
