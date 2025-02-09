from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt6.QtGui import QIcon
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 QTabelWidget")
        self.setWindowIcon(QIcon('images/icon.png'))

        vbox = QVBoxLayout()

        table = QTableWidget()
        table.setRowCount(5)
        table.setColumnCount(3)

        table.setItem(0, 0, QTableWidgetItem("Name"))
        table.setItem(0, 1, QTableWidgetItem("Age"))
        table.setItem(0, 2, QTableWidgetItem("Email"))

        table.setItem(1, 0, QTableWidgetItem("John Doe"))
        table.setItem(1, 1, QTableWidgetItem("25"))
        table.setItem(1, 2, QTableWidgetItem("doe@gmail.com"))

        table.setItem(2, 0, QTableWidgetItem("Jane Doe"))
        table.setItem(2, 1, QTableWidgetItem("22"))
        table.setItem(2, 2, QTableWidgetItem("doe@yahoo.com"))

        table.setItem(3, 0, QTableWidgetItem("John Smith"))
        table.setItem(3, 1, QTableWidgetItem("30"))
        table.setItem(3, 2, QTableWidgetItem("smith@lastking.com"))

        table.setItem(4, 0, QTableWidgetItem("Jane Smith"))
        table.setItem(4, 1, QTableWidgetItem("28"))
        table.setItem(4, 2, QTableWidgetItem("jane@wisecode.com"))
        

        vbox.addWidget(table)

        self.setLayout(vbox)


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())