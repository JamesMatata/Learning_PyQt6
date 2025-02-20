# This allows developer to build apps that communicate with web servers and retrieve some data
# To handle network requests in PyQt6 you use the following components:
# - QNetworkAccessManager - This class is resposible for managing network requests and sending them to the server. It provides methods to send http GET, POST, PUT, DELETE requests and other types of requests. It also emits signals when a request is finished or when an error occurs.
# - QNetworkRequest - This class represents an http request. It allows you to set header, specify the request methods and provide the target url.
# - QNetworkReply - This class represents the response from the server. It provides methods to read the response data, get the response headers and handle errors.

# Practical Example
from  PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QTextEdit
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
import sys
from PyQt6.QtCore import QUrl

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 REST API Example")
        self.setGeometry(100, 100, 800, 600)

        vbox = QVBoxLayout()

        url_label = QLabel("Enter URL:")

        self.input = QLineEdit()

        send_button = QPushButton("Send Request")
        send_button.clicked.connect(self.send_request)

        response_label = QLabel("Response:")
        self.response = QTextEdit()
        self.response.setReadOnly(True)

        vbox.addWidget(url_label)
        vbox.addWidget(self.input)
        vbox.addWidget(send_button)
        vbox.addWidget(response_label)
        vbox.addWidget(self.response)

        self.setLayout(vbox)

        self.network_manager = QNetworkAccessManager()
        self.network_manager.finished.connect(self.handle_response)

    def send_request(self):
        url = self.input.text()
        request = QNetworkRequest(QUrl(url))
        self.network_manager.get(request)

    def handle_response(self, reply):
        error = reply.error()
        if error == QNetworkReply.NetworkError.NoError:
            response = reply.readAll().data().decode("utf-8")
            self.response.setPlainText(response)
        else:
            self.response.setPlainText(f"Error: {reply.errorString()}")

    def closeEvent(self, event):
        self.network_manager.deleteLater()
        super().closeEvent(event)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())