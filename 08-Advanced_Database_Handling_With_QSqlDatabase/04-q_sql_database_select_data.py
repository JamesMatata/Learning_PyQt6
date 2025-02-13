from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTableView
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt6.QtCore import Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6  QSqlDatabase Select Data")
        self.setWindowIcon(QIcon('images/icon.png'))
       
        vbox = QVBoxLayout()

        self.table = QTableView()
        

        self.result = QLabel()
        self.result.setFont(QFont('Arial', 15))
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result.setStyleSheet("margin-top: 10px;font-weight: bold;")

        vbox.addWidget(self.table)
        vbox.addWidget(self.result)

        self.setLayout(vbox)

        self.connect_database()

    def connect_database(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('example.db')
        if db.open():
            self.fetch_data()
            self.result.setText("Data Displayed Successfully")
            self.result.setStyleSheet("color: green;")

        else:
            self.result.setText("Failed to connect to the database")
            self.result.setStyleSheet("color: red;")
            print(db.lastError().text())

    def fetch_data(self):
        model = QSqlQueryModel()
        model.setQuery("SELECT * FROM employees")

        self.table.setModel(model)




app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())