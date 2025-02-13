from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtSql import QSqlDatabase
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 QSqlDatabase")
        self.setWindowIcon(QIcon('images/icon.png'))

        vbox = QVBoxLayout()

        self.label = QLabel()
        self.label.setFont(QFont('Arial', 15))

        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.create_connection()

    def create_connection(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('example.db')

        if not db.open():
            self.label.setText("Failed to open the database")
            # To check the error which occurred while opening the database
            print(db.lastError().text())
        else:
            self.label.setText("Database connected successfully")

        db.close()

app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())