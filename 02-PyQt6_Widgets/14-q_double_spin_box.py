from PyQt6.QtWidgets import QApplication, QWidget, QDoubleSpinBox, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout
from PyQt6.QtGui import QIcon
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 70)
        self.setWindowTitle("PyQt6 QDoubleSpinBox")
        self.setWindowIcon(QIcon('images/icon.png'))

        hbox = QHBoxLayout()

        label = QLabel("Sugar Cost:")
        label.setStyleSheet('font-size: 15px; font-weight: bold;')
        
        self.pricevbox = QVBoxLayout()
        self.label2 = QLabel("@Price:")
        self.line_edit = QLineEdit()
        self.line_edit.setText("1")
        self.pricevbox.addWidget(self.label2)
        self.pricevbox.addWidget(self.line_edit)

    
        self.totalvbox = QVBoxLayout()
        self.label3 = QLabel("Total:")
        self.results = QLineEdit()
        self.totalvbox.addWidget(self.label3)
        self.totalvbox.addWidget(self.results)

        self.qtyvbox = QVBoxLayout()
        self.label4 = QLabel("Qty:")
        self.spin_box = QDoubleSpinBox()
        self.spin_box.valueChanged.connect(self.spin_selected)
        self.qtyvbox.addWidget(self.label4)
        self.qtyvbox.addWidget(self.spin_box)




        hbox.addWidget(label)
        hbox.addLayout(self.pricevbox)
        hbox.addLayout(self.qtyvbox)
        hbox.addLayout(self.totalvbox)


        self.setLayout(hbox)

    def spin_selected(self):
        if self.line_edit.text() != 0:
            price = int(self.line_edit.text())
            quantity = self.spin_box.value()
            total = price * quantity
            self.results.setText(str(total))

        else:
            self.results.setText("N/A")


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())