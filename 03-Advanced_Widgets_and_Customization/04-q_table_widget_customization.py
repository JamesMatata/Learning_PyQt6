from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QIcon
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 400, 250)
        self.setWindowTitle("PyQt6 QTabelWidget Customization")
        self.setWindowIcon(QIcon('images/icon.png'))

        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)

        self.setupr_table()

    def setupr_table(self):
        self.table_widget.setColumnCount(3)
        self.table_widget.setRowCount(5)

        for row in range(self.table_widget.rowCount()):
            for col in range(self.table_widget.columnCount()):
                item = QTableWidgetItem(f"Row {row + 1} Col {col + 1}")
                self.table_widget.setItem(row, col, item)

        self.table_widget.setStyleSheet(
            """
            QTableWidget {
                background-color: #F5F5F5;
                font-family: 'Arial';
                border: 1px solid blue;
                color: #333;
            }

            QTableWidget::item {
            padding: 10px;
            border: 1px solid #ccc;
            }

            QTableWidget::item:selected {
            background-color: blue;
            color: white;
            }
            
            QTableWidget::item:selected:!active {
            background-color: darkblue;
            color: white;
            }

        """
        )



app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())