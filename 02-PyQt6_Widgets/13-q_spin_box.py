from PyQt6.QtWidgets import QApplication, QWidget, QSpinBox, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 100)
        self.setWindowTitle("PyQt6 QSpinBox")
        self.setWindowIcon(QIcon('images/icon.png'))

        hbox = QHBoxLayout()

        label = QLabel("Laptop price:")
        label.setStyleSheet('font-size: 15px; font-weight: bold;')
        
        self.pricevbox = QVBoxLayout()
        self.label2 = QLabel("Price:")
        self.line_edit = QLineEdit()
        self.line_edit.setText("1")
        self.pricevbox.addWidget(self.label2)
        self.pricevbox.addWidget(self.line_edit)

    
        self.totalvbox = QVBoxLayout()
        self.label3 = QLabel("Total:")
        self.results = QLineEdit()
        self.results.setReadOnly(True)
        self.totalvbox.addWidget(self.label3)
        self.totalvbox.addWidget(self.results)

        self.qtyvbox = QVBoxLayout()
        self.label4 = QLabel("Qty:")
        self.spin_box = QSpinBox()
        # Using the valueChanged signal
        self.spin_box.valueChanged.connect(self.spin_selected)
        # Using the desitingFinished signal
        self.spin_box.editingFinished.connect(self.final_price)
        self.qtyvbox.addWidget(self.label4)
        self.qtyvbox.addWidget(self.spin_box)

        self.final_price = QLabel("Final Price: <-->")
        self.final_price.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.final_price.setStyleSheet('font-size: 15px; font-weight: bold;')

        hbox.addWidget(label)
        hbox.addLayout(self.pricevbox)
        hbox.addLayout(self.qtyvbox)
        hbox.addLayout(self.totalvbox)

        mainvbox = QVBoxLayout()
        mainvbox.addLayout(hbox)
        mainvbox.addWidget(self.final_price)


        self.setLayout(mainvbox)

    def spin_selected(self):
        if self.line_edit.text() != 0:
            price = int(self.line_edit.text())
            quantity = self.spin_box.value()
            total = price * quantity
            self.results.setText(str(total))

        else:
            self.results.setText("Please enter a price")

    def final_price(self):
        if self.line_edit.text() != 0:
            price = int(self.line_edit.text())
            quantity = self.spin_box.value()
            total = price * quantity
            self.final_price.setText(f"Spend {str(total)} on sugar")

        else:
            self.results.setText("Enter valid price")
        


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())