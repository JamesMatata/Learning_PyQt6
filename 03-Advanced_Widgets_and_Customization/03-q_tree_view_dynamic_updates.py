from PyQt6.QtWidgets import QApplication, QTreeView, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon, QFileSystemModel
from PyQt6.QtCore import Qt, QFileSystemWatcher, QModelIndex
import sys, os

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 QTreeView")
        self.setWindowIcon(QIcon('images/icon.png'))

        self.tree = QTreeView()

        self.model = QFileSystemModel()
        self.model.setRootPath('')

        self.tree.setModel(self.model)

        layout = QVBoxLayout()

        layout.addWidget(self.tree)

        main_widget = QWidget()

        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        self.setup_file_watcher()

    def setup_file_watcher(self):
        self.file_watcher = QFileSystemWatcher()
        self.file_watcher.directoryChanged.connect(self.directory_changed)
        self.file_watcher.fileChanged.connect(self.file_changed)

    def directory_changed(self, directory):
        index = self.model.index(directory)
        self.tree.update(index)

    def file_changed(self, file):
        directory = os.path.dirname(file)
        index = self.model.index(directory)
        self.tree.update(index)

    def add_directory_to_watch(self, directory):
        self.file_watcher.addPath(directory)


app = QApplication(sys.argv)
window = window()
window.add_directory_to_watch(os.getcwd())
window.show()
sys.exit(app.exec())