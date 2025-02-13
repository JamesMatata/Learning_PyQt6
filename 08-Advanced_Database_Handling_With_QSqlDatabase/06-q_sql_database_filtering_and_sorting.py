from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTableView, QLineEdit
from PyQt6.QtGui import QIcon
from PyQt6.QtSql import QSqlDatabase, QSqlQueryModel
from PyQt6.QtCore import Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 500, 250)
        self.setWindowTitle("PyQt6 QSqlDatabase Filtering and Sorting")
        self.setWindowIcon(QIcon('images/icon.png'))

        vbox = QVBoxLayout()

        self.filter_input = QLineEdit()
        self.filter_input.setPlaceholderText("Enter a name to filter")
        self.filter_input.textChanged.connect(self.filter_data)
        self.table = QTableView()
        self.result = QLabel()
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        vbox.addWidget(self.filter_input)
        vbox.addWidget(self.table)
        vbox.addWidget(self.result)

        self.setLayout(vbox)

        self.connect_database()
        self.fetch_data()

    def connect_database(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('example.db')
        if db.open():
            self.result.setText("Database Connected Successfully")
            self.result.setStyleSheet("color: green;")

        else:
            self.result.setText("Failed to connect to the database")
            self.result.setStyleSheet("color: red;")
            print(db.lastError().text())

    def fetch_data(self):
        model = QSqlQueryModel()
        model.setQuery("SELECT * FROM employees")

        self.table.setModel(model)

    def filter_data(self):
        filter_text = self.filter_input.text()

        model = self.table.model()

        base_query = "SELECT * FROM employees"

        if filter_text:
           modified_query = base_query + f" WHERE name LIKE '{filter_text}%'"
        else:
            modified_query = base_query

        model.setQuery(modified_query)


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())