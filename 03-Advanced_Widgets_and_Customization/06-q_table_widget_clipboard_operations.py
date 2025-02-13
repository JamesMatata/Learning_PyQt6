from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView, QMenu
from PyQt6 import QtGui
from PyQt6.QtGui import QIcon, QAction, QKeySequence
from PyQt6.QtCore import Qt, QMimeData
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 QTableWidget Clipboard Operations")
        self.setWindowIcon(QIcon('images/icon.png'))

        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)

        self.setup_tabel()


    def setup_tabel(self):
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Name", "Age", "Email"])
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        data = [
            ("Alice", "25", "alice@gmail.com"),
            ("Bob", "30", "bob@gmail.com"),
            ("Charlie", "35", "charlie@gmail.com")
        ]

        self.table_widget.setRowCount(len(data))

        for row, (name, age, email) in enumerate(data):
            self.table_widget.setItem(row, 0, QTableWidgetItem(name))
            self.table_widget.setItem(row, 1, QTableWidgetItem(age))
            self.table_widget.setItem(row, 2, QTableWidgetItem(email))

        self.table_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.create_context_menu_actions()
        self.table_widget.addAction(self.copy_action)
        self.table_widget.addAction(self.paste_action)

    def create_context_menu_actions(self):
        self.copy_action = QAction("Copy", self)
        self.copy_action.setShortcut(QKeySequence.StandardKey.Copy)
        self.copy_action.triggered.connect(self.copy_selected_cell)

        self.paste_action = QAction("Paste", self)
        self.paste_action.setShortcut(QKeySequence.StandardKey.Paste)
        self.paste_action.triggered.connect(self.paste_selected_cell)

    def copy_selected_cell(self):
        selection = self.table_widget.selectedRanges()
        if not selection:
            return
        cells_text = []

        for selection_range in selection:
            for row in range(selection_range.topRow(), selection_range.bottomRow() + 1):
                for col in range(selection_range.leftColumn(), selection_range.rightColumn() + 1):
                    item = self.table_widget.item(row, col)
                    if item:
                        cells_text.append(item.text())
        mime_data = QMimeData()
        mime_data.setText("\t".join(cells_text))
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mime_data)


    def paste_selected_cell(self):
        clipboard = QApplication.clipboard()
        mime_data = clipboard.mimeData()

        if mime_data.hasText():
            text = mime_data.text()
            cells_text = text.split("\t")

            current_range = self.table_widget.selectedRanges()[0]
            top_row = current_range.topRow()
            left_column = current_range.leftColumn()

            for row in range(current_range.rowCount()):
                for colun in range(current_range.columnCount()):
                    item = self.table_widget.item(top_row + row, left_column + colun)
                    if item:
                        if cells_text:
                            item.setText(cells_text.pop(0))
                        else:
                            return
                        
    def contextMenuEvent(self, event):
        context_menu = QMenu()
        context_menu.addAction(self.copy_action)
        context_menu.addAction(self.paste_action)
        context_menu.exec(event.globalPos())

            


app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())