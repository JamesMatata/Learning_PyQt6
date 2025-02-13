from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTableView, QLineEdit, QPushButton
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt6.QtCore import Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 400)
        self.setWindowTitle("PyQt6  QSqlDatabase Update Data")
        self.setWindowIcon(QIcon('images/icon.png'))
       
        vbox = QVBoxLayout()

        self.id_imput = QLineEdit()
        self.name_imput = QLineEdit()
        self.email_imput = QLineEdit()
        self.age_imput = QLineEdit()
        button = QPushButton("Update Data")
        button.clicked.connect(self.update_data)

        self.table = QTableView()
        

        self.result = QLabel()
        self.result.setFont(QFont('Arial', 15))
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result.setStyleSheet("margin-top: 10px;font-weight: bold;")
        vbox.addWidget(QLabel("ID:"))
        vbox.addWidget(self.id_imput)
        vbox.addWidget(QLabel("Name:"))
        vbox.addWidget(self.name_imput)
        vbox.addWidget(QLabel("Email:"))
        vbox.addWidget(self.email_imput)
        vbox.addWidget(QLabel("Age:"))
        vbox.addWidget(self.age_imput)
        vbox.addWidget(button)

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

    def update_data(self):
        id_no = int(self.id_imput.text())
        name = self.name_imput.text()
        email = self.email_imput.text()
        age = int(self.age_imput.text())

        if not id_no or not name or not email or not age:
            self.result.setText("All fields are required")
            self.result.setStyleSheet("color: red;")
            return
        query = QSqlQuery()
        update_query = "UPDATE employees SET name = :name, email = :email, age = :age WHERE id = :id"
        query.prepare(update_query)
        query.bindValue(':name', name)
        query.bindValue(':email', email)
        query.bindValue(':age', age)
        query.bindValue(':id', id_no)

        if query.exec():
            self.result.setText("Data Updated Successfully")
            self.result.setStyleSheet("color: green;")
            self.id_imput.clear()
            self.name_imput.clear()
            self.email_imput.clear()
            self.age_imput.clear()
            self.fetch_data()
        else:
            self.result.setText("Failed to update data")
            self.result.setStyleSheet("color: red;")
            print(query.lastError().text())


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())