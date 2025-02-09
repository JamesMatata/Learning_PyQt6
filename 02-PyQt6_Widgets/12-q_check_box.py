from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QHBoxLayout, QVBoxLayout, QLabel 
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize, Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 150)
        self.setWindowTitle("PyQt6 QCheckBox")
        self.setWindowIcon(QIcon('images/icon.png'))

        hbox = QHBoxLayout()

        self.title = QLabel("Select your favourite programming languages")
        self.title.setStyleSheet('font-size: 15px; font-weight: bold;')

        self.checkbox1 = QCheckBox('Python')
        self.checkbox1.setIcon(QIcon('C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs/Learning_GUIs_with_PyQt6/02-PyQt6_Widgets/images/py.png'))
        self.checkbox1.setIconSize(QSize(25,25))
        self.checkbox1.stateChanged.connect(self.checkbox_selected)

        self.checkbox2 = QCheckBox('Java')
        self.checkbox2.setIcon(QIcon('C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs/Learning_GUIs_with_PyQt6/02-PyQt6_Widgets/images/java.png'))
        self.checkbox2.setIconSize(QSize(25,25))
        self.checkbox2.stateChanged.connect(self.checkbox_selected)

        self.checkbox3 = QCheckBox('JavaScript')
        self.checkbox3.setIcon(QIcon('C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs/Learning_GUIs_with_PyQt6/02-PyQt6_Widgets/images/js.png'))
        self.checkbox3.setIconSize(QSize(25,25))
        self.checkbox3.stateChanged.connect(self.checkbox_selected)

        self.checkbox4 = QCheckBox('C++')
        self.checkbox4.setIcon(QIcon('C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs/Learning_GUIs_with_PyQt6/02-PyQt6_Widgets/images/cplusplus.png'))
        self.checkbox4.setIconSize(QSize(25,25))
        self.checkbox4.stateChanged.connect(self.checkbox_selected)

        hbox.addWidget(self.checkbox1)
        hbox.addWidget(self.checkbox2)
        hbox.addWidget(self.checkbox3)
        hbox.addWidget(self.checkbox4)

        self.label = QLabel("---(-)-----======----(-)---")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet('font-size: 14px; font-weight: bold;color: red;')

        vbox = QVBoxLayout()

        topvbox = QVBoxLayout()

        topvbox.addWidget(self.title)
        topvbox.addLayout(hbox)

        vbox.addLayout(topvbox)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def checkbox_selected(self):
        value = ""
        if self.checkbox1.isChecked():
            if value:
                value += ', '
            value += self.checkbox1.text()

        if self.checkbox2.isChecked():
            if value:
                value += ', '
            value += self.checkbox2.text()

        if self.checkbox3.isChecked():
            if value:
                value += ', '
            value += self.checkbox3.text()

        if self.checkbox4.isChecked():
            if value:
                value += ' and '
            value += self.checkbox4.text()

        if value:
            self.label.setText(f'You favourite: {value}')
        else:
            self.label.setText("---(-)-----======----(-)---")


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())