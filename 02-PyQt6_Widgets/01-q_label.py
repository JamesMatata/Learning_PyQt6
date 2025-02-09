from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt6 import QtCore
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QLabel")
        self.setWindowIcon(QIcon('../images/icon.png'))

        # label = QLabel("Python GUI Development with PyQt6", self)
        # # Set the text of the Label
        # label.setText("New Text is here")
        # # Set the alignment of the text/Move the text
        # label.move(20,100)
        # # Set the font of the text
        # label.setFont(QFont('Sanserif', 20))
        # label.setStyleSheet('color: red')

        # # Set the text of the Label to have a number
        # label.setText(str(12))
        # # Or
        # label.setNum(17)
        # # To clear the label
        # label.clear()

        # label = QLabel(self)
        # pixmap = QPixmap('images/icon.png')
        # label.setPixmap(pixmap)

        # QMovie is used to show simple animation without sound
        label = QLabel(self)
        movie = QMovie('C:/Users/James Matata/Desktop/CodeWizard/Python_Programming/Learning_Python_GUIs/Learning_GUIs_with_PyQt6/02-PyQt6_Widgets/images/anim.gif')
        movie.setSpeed(100)
        label.setMovie(movie)
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        movie.start()





app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())