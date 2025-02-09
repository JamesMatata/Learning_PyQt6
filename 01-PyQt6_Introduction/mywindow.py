# Import necessary modules from PyQt6
from PyQt6.QtWidgets import QApplication, QWidget
import sys  # sys module is needed for handling system-specific parameters

# Create an instance of QApplication. This is required to start any PyQt application.
# sys.argv allows passing command-line arguments to the application (if needed).
app = QApplication(sys.argv)

# Create an instance of a QWidget (this is a basic window or widget).
window = QWidget()

# Show the window to the user. This makes the window appear on the screen.
window.show()

# Start the application's event loop. This will wait for events (like button clicks, closing the window, etc.)
# sys.exit() ensures that the program exits properly when the event loop ends.
sys.exit(app.exec())
