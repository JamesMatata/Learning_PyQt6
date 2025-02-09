from PyQt6.QtWidgets import QApplication, QWidget, QTreeView, QMainWindow
from PyQt6.QtGui import QIcon, QStandardItem, QStandardItemModel
import sys

class TreeViewWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 QTreeView")
        self.setWindowIcon(QIcon('images/icon.png'))


        self.tree = QTreeView()
        self.setCentralWidget(self.tree)

        self.model = QStandardItemModel()
        self.tree.setModel(self.model)

        self.file_explorer()


    def file_explorer(self):
        root_item = QStandardItem("Root")
        self.model.appendRow(root_item)

        folder_item = QStandardItem("Folder 1")
        file_item = QStandardItem("File 1")
        file_item.setIcon(QIcon('images/icon.png'))
        file_item.setToolTip("This is a file")
        root_item.appendRow(folder_item)
        folder_item.appendRow(file_item)


app = QApplication(sys.argv)
window = TreeViewWindow()
window.show()
sys.exit(app.exec())