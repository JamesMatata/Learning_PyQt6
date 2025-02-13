from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtSql import QSqlDatabase,QSqlQuery
from PyQt6.QtCore import Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 QSqlDatabase insert Data")
        self.setWindowIcon(QIcon('images/icon.png'))

        self.setStyleSheet("""
        QPushButton {
            background-color: blue;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
                           border-radius: 2px;
                           border: none;
        }
                           QLineEdit {
                           padding: 10px;
                           font-size: 16px;
                           border: 1px solid blue;
                           }

        """)

        vbox = QVBoxLayout()

        self.name_imput = QLineEdit()
        self.email_imput = QLineEdit()
        self.age_imput = QLineEdit()

        self.insert_button = QPushButton("Insert Data")
        self.insert_button.clicked.connect(self.insert_data)

        self.result = QLabel()
        self.result.setFont(QFont('Arial', 15))
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result.setStyleSheet("margin-top: 10px;font-weight: bold;")

        vbox.addWidget(QLabel("Name"))
        vbox.addWidget(self.name_imput)
        vbox.addWidget(QLabel("Email"))
        vbox.addWidget(self.email_imput)
        vbox.addWidget(QLabel("Age"))
        vbox.addWidget(self.age_imput)
        vbox.addWidget(self.insert_button)
        vbox.addWidget(self.result)

        self.setLayout(vbox)

        self.connect_database()

    def connect_database(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('example.db')
        if db.open():
            self.result.setText("Database connected successfully")
            self.result.setStyleSheet("color: green;")

        else:
            self.result.setText("Failed to connect to the database")
            self.result.setStyleSheet("color: red;")
            print(db.lastError().text())

    def insert_data(self):
        name = self.name_imput.text()
        email = self.email_imput.text()
        age = self.age_imput.text()

        if not name or not age or not email:
            self.result.setText("Please fill all the fields")
            self.result.setStyleSheet("color: red;")
            return
        query = QSqlQuery()

        insert_query = "INSERT INTO employees(name, email, age) VALUES(:name, :email, :age)"
        query.prepare(insert_query)
        query.bindValue(':name', name)
        query.bindValue(':email', email)
        query.bindValue(':age', age)

        if query.exec():
            self.result.setText("Data inserted successfully")
            self.result.setStyleSheet("color: green;")
            self.name_imput.clear()
            self.email_imput.clear()
            self.age_imput.clear()
        else:
            self.result.setText("Failed to insert data")
            self.result.setStyleSheet("color: red;")
            print(query.lastError().text())




app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())