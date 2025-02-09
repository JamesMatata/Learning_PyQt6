from PyQt6.QtWidgets import QApplication, QWidget, QListWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 280)
        self.setWindowTitle("PyQt6 QListWidget")
        self.setWindowIcon(QIcon('images/icon.png'))

        hbox = QHBoxLayout()
        self.title = QLabel("Favorite Programming languages")
        self.title.setFont(QFont('Arial', 15))
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("margin-bottom: 10px;")

        self.add_button = QPushButton("Add Language")
        self.add_button.setStyleSheet("background-color: lightblue; color: black;padding: 10px;font-size: 14px;font-weight: bold;border-radius: 3px;")
        self.add_button.clicked.connect(self.add_language)

        self.language = QLineEdit()
        self.language.setPlaceholderText("Enter language")
        self.language.setStyleSheet("padding: 10px; font-size: 14px; border-radius: 3px;border: 1px solid lightgray;")

        hbox.addWidget(self.language)
        hbox.addWidget(self.add_button)

        vbox = QVBoxLayout()

        self.list_widget = QListWidget()

        self.list_widget.insertItem(0, "C++")
        self.list_widget.insertItem(1, "Java")
        self.list_widget.insertItem(2, "Python")
        self.list_widget.insertItem(3, "C#")
        self.list_widget.insertItem(4, "JavaScript")
        self.list_widget.insertItem(5, "Ruby")

        self.list_widget.setFont(QFont('Arial', 13))

        self.list_widget.setStyleSheet("background-color: lightgray; color: black;")

        self.list_widget.clicked.connect(self.item_clicked)

        self.label = QLabel("---[]----[]---")
        self.label.setFont(QFont('Arial', 15))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        vbox.addWidget(self.title)
        vbox.addLayout(hbox)
        vbox.addWidget(self.list_widget)
        vbox.addWidget(self.label)

        self.setLayout(vbox)


    def item_clicked(self):
        self.label.setText(f"{self.list_widget.currentItem().text()} Selected")

    def add_language(self):
        language = self.language.text()
        if language:
            self.list_widget.addItem(language)
            self.language.clear()
            self.language.setStyleSheet("padding: 10px; font-size: 14px; border-radius: 3px;border: 1px solid lightgray;")
        else:
            self.language.setStyleSheet("padding: 10px; font-size: 14px; border-radius: 3px;border: 1px solid red;")


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())