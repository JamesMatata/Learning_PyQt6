from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
import sys
from PyQt6.QtNetwork import QTcpSocket, QHostAddress


class ClientWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Client")
        self.setGeometry(100, 100, 400, 300)

        self.line = QLineEdit(self)
        self.line.setGeometry(50, 50, 150, 30)

        button = QPushButton("Send", self)
        button.setGeometry(50, 100, 150, 30)
        button.clicked.connect(self.send_message)

        self.client_socket = QTcpSocket(self)
        self.client_socket.connected.connect(self.connected)
        self.client_socket.readyRead.connect(self.receive_message)
        self.client_socket.disconnected.connect(self.disconnected)
        self.client_socket.errorOccurred.connect(self.display_error)
        self.client_socket.connectToHost("localhost", 8888)

    def connected(self):
        print("Connected to server")

    def disconnected(self):
        print("Disconnected from server")

    def display_error(self, socket_error):
        print(f"Error: {socket_error}")

    def receive_message(self):
        message = self.client_socket.readAll().data().decode()
        print(f"Received message from server: {message}")

    def send_message(self):
        message = self.line.text()
        self.client_socket.write(message.encode())
        self.line.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ClientWindow()
    window.show()

    sys.exit(app.exec())