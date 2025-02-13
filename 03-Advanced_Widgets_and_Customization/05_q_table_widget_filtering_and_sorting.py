from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QLineEdit, QWidget, QHeaderView
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 500, 250)
        self.setWindowTitle("PyQt6 QTableWidget Sorting and Filtering")
        self.setWindowIcon(QIcon('images/icon.png'))

        self.table_widget = QTableWidget()

        self.filter_input = QLineEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(self.filter_input)
        vbox.addWidget(self.table_widget)

        main_widget = QWidget()
        main_widget.setLayout(vbox)

        self.setCentralWidget(main_widget)

        self.setup_table()
        self.setup_connections()

    def setup_table(self):
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["Name", "Category", "Price", "Date" ])

        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        data = [
            ("Mangoes", "category1", "200", "2021-01-01"),
            ("Oranges", "category2", "280", "2021-02-07"),
            ("Lemons", "category2", "125", "2021-01-19"),
            ("Apples", "category4", "470", "2021-08-05"),
            ("Water Melons", "category3", "290", "2021-12-27"),
        ]

        self.table_widget.setRowCount(len(data))

        for row, (name, category, price, date) in enumerate(data):
            self.table_widget.setItem(row, 0, QTableWidgetItem(name))
            self.table_widget.setItem(row, 1, QTableWidgetItem(category))
            self.table_widget.setItem(row, 2, QTableWidgetItem(price))
            self.table_widget.setItem(row, 3, QTableWidgetItem(date))


    def setup_connections(self):
        self.table_widget.horizontalHeader().sectionClicked.connect(self.sort_table)
        self.filter_input.textChanged.connect(self.filter_table)

    def sort_table(self, column):
        self.table_widget.sortItems(column, Qt.SortOrder.AscendingOrder)

    def filter_table(self, text):
        for row in range(self.table_widget.rowCount()):
            match = False
            for col in range(self.table_widget.columnCount()):
                item = self.table_widget.item(row, col)
                if text.lower() in item.text().lower():
                    match = True
                    break
            self.table_widget.setRowHidden(row, not match)
            


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())