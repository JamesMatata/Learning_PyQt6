from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtSql import QSqlDatabase,QSqlQuery
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 QSqlDatabase Tabel Creation")
        self.setWindowIcon(QIcon('images/icon.png'))

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('example.db')

        if not db.open():
            print(db.lastError().text())
            sys.exit(1)
        else:
            print("Database connected successfully")

        query = QSqlQuery()
        create_table = """
            CREATE TABLE IF NOT EXISTS employees(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        """
        query.exec(create_table)

        if not query.exec(create_table):
            print(query.lastError().text())
            sys.exit(1)

        db.close()

        


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())