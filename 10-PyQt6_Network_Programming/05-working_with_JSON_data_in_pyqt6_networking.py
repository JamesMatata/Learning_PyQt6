from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QUrl
import sys, json
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 Working with JSON Data")
        self.setWindowIcon(QIcon('images/icon.png'))

        vbox = QVBoxLayout()

        self.text_edit = QTextEdit()
        self.text_edit.setMinimumHeight(300)

        vbox.addWidget(self.text_edit)

        button = QPushButton("Fetch Data")
        button.clicked.connect(self.fetch_json)
        vbox.addWidget(button)

        self.setLayout(vbox)

        self.network_manager = QNetworkAccessManager(self)
        self.network_manager.finished.connect(self.handle_response)

    def handle_response(self, reply: QNetworkReply):
        if reply.error() != QNetworkReply.NetworkError.NoError:
            self.text_edit.setText(f"Error: {reply.errorString()}")
        else:
            response = reply.readAll().data().decode()
            json_data = json.loads(response)

            self.text_edit.setPlainText(f"Received JSON Data:")
            for item in json_data:
                self.text_edit.append(f"Title : {item['title']}")
                self.text_edit.append(f"Body : {item['body']}")
                self.text_edit.append("\n-----------------------------------------------------------\n")

    def fetch_json(self):
        url = QUrl("https://jsonplaceholder.typicode.com/posts")
        request = QNetworkRequest(url)
        self.network_manager.get(request)


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())