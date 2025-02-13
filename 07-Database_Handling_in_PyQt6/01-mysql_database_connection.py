import sys
import mysql.connector as mc
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class DatabaseApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Database Connection")
        self.resize(400, 180)

        # Styling
        self.setStyleSheet("""
            QPushButton {
                padding: 10px;
                border: none;
                border-radius: 5px;
                color: white;
                font-size: 16px;
            }
            QPushButton#btn_create { background-color: blue; }
            QPushButton#btn_connect { background-color: darkblue; }
            QLineEdit { padding: 10px; border: 1px solid blue; border-radius: 2px; }
            QLabel#lbl_result { font-size: 14px; font-weight: bold; color: black; }
        """)

        # Layouts
        layout = QtWidgets.QVBoxLayout(self)

        # Database Name Input
        db_layout = QtWidgets.QHBoxLayout()
        self.lbl_name = QtWidgets.QLabel("Database Name:")
        self.lbl_name.setFont(QtGui.QFont("", 12, QtGui.QFont.Weight.Bold))
        self.txt_db = QtWidgets.QLineEdit()
        db_layout.addWidget(self.lbl_name)
        db_layout.addWidget(self.txt_db)
        layout.addLayout(db_layout)

        # Buttons
        btn_layout = QtWidgets.QHBoxLayout()
        self.btn_create = QtWidgets.QPushButton("Create Database")
        self.btn_create.setObjectName("btn_create")
        self.btn_create.clicked.connect(self.create_database)

        self.btn_connect = QtWidgets.QPushButton("Connect to Database")
        self.btn_connect.setObjectName("btn_connect")
        self.btn_connect.clicked.connect(self.connect_database)

        btn_layout.addWidget(self.btn_create)
        btn_layout.addWidget(self.btn_connect)
        layout.addLayout(btn_layout)

        # Result Display
        self.lbl_result = QtWidgets.QLabel("---[]----[]---")
        self.lbl_result.setObjectName("lbl_result")
        self.lbl_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.lbl_result)

    def create_database(self):
        """Creates a MySQL database."""
        dbname = self.txt_db.text().strip()
        if not dbname:
            self.lbl_result.setText("Database Name is required")
            self.lbl_result.setStyleSheet("color: red;")
            return

        try:
            conn = mc.connect(
                host="localhost",
                user="root",
                password="jamesMATATA"  # Change this if you have a password
            )
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE `{dbname}`")  # Use backticks for special characters
            self.lbl_result.setText(f"Database '{dbname}' created successfully!")
            self.lbl_result.setStyleSheet("color: green;")

            cursor.close()
            conn.close()
        except mc.Error as err:
            self.lbl_result.setText(f"Error: {err}")
            self.lbl_result.setStyleSheet("color: red;")

    def connect_database(self):
        """Connects to an existing MySQL database."""
        dbname = self.txt_db.text().strip()
        if not dbname:
            self.lbl_result.setText("Database Name is required")
            self.lbl_result.setStyleSheet("color: red;")
            return

        try:
            conn = mc.connect(
                host="localhost",
                user="root",
                password="jamesMATATA",  # Change this if needed
                database=dbname
            )
            if conn.is_connected():
                self.lbl_result.setText(f"Connected to '{dbname}' successfully!")
                self.lbl_result.setStyleSheet("color: green;")
            conn.close()
        except mc.Error as err:
            self.lbl_result.setText(f"Connection Error: {err}")
            self.lbl_result.setStyleSheet("color: red;")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DatabaseApp()
    window.show()
    sys.exit(app.exec())