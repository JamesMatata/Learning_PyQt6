from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QTableView, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QSplitter, QWidget, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 800, 400)
        self.setWindowTitle("PyQt6 ")
        self.setWindowIcon(QIcon('images/icon.png'))

        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #060608;
            }
            QTableView {
            background-color: #060608;
            }
            QLabel {
            color: white;
            font-size: 16px;
            font-weight: bold;
            }
            QLineEdit {
            color: white;
            border: 1px solid white;
            border-radius: 2px;
            padding: 7px;
            font-size: 14px;
            background-color: #060608;
            }
            QPushButton {
            color: white;
            border: none;
            border-radius: 2px;
            padding: 7px;
            font-size: 14px;
            background-color: darkblue;
            }
            """
        )

        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)

        splitter = QSplitter()

        left_widget = QWidget()
        left_vbox = QVBoxLayout(left_widget)
        top_hbox = QHBoxLayout()
        self.table_title = QLabel("Employee List")
        self.add_new = QPushButton("Add New Employee")
        top_hbox.addWidget(self.table_title)
        top_hbox.addWidget(self.add_new)
        self.table = QTableView()
        left_vbox.addLayout(top_hbox)
        left_vbox.addWidget(self.table)

        right_widget = QWidget()
        right_widget.setFixedWidth(250)  # Fix width
        right_vbox = QVBoxLayout(right_widget)
        self.form_title = QLabel("Change Details")
        self.first_name = QLineEdit()
        self.first_name.setPlaceholderText("First Name")
        self.last_name = QLineEdit()
        self.last_name.setPlaceholderText("Last Name")
        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")
        self.phone_number = QLineEdit()
        self.phone_number.setPlaceholderText("Phone Number")
        self.department = QLineEdit()
        self.department.setPlaceholderText("Department")
        self.salary = QLineEdit()
        self.salary.setPlaceholderText("Salary")
        self.update_button = QPushButton("Update Data")
        self.status = QLabel()
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        right_vbox.addWidget(self.form_title)
        right_vbox.addWidget(self.first_name)
        right_vbox.addWidget(self.last_name)
        right_vbox.addWidget(self.email)
        right_vbox.addWidget(self.phone_number)
        right_vbox.addWidget(self.department)
        right_vbox.addWidget(self.salary)
        right_vbox.addWidget(self.update_button)
        right_vbox.addWidget(self.status)
        right_vbox.addItem(self.spacer)

        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)

        splitter.setSizes([550, 250])

        main_layout.addWidget(splitter)

        self.setCentralWidget(main_widget)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
