from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QObject, pyqtSignal, QEvent
import sys

class CustomEvent(QEvent):
    Type = QEvent.registerEventType()

    def __init__(self, message):
        super().__init__(CustomEvent.Type)
        self.message = message

class CustomEventEmitter(QObject):
    custom_event = pyqtSignal(CustomEvent)

    def emit_custom_event(self, message):
        event = CustomEvent(message)
        self.custom_event.emit(event)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 Custom Event Handling")
        
        self.label = QLabel("No custom event emitted yet", self)
        self.label.setStyleSheet("padding: 10px;")
        self.label.setGeometry(50, 50, 300, 150)

        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def custom_event_handler(self, event):
        self.label.setText(event.message)

    def custom_event_filter(self, obj, event):
        if event.type() == CustomEvent.Type:
            self.custom_event_handler(event)
            return True
        return False
    

app = QApplication(sys.argv)
window = MainWindow()
emitter = CustomEventEmitter()
emitter.custom_event.connect(window.custom_event_handler)
emitter.emit_custom_event("Custom event emitted")
window.show()
sys.exit(app.exec())