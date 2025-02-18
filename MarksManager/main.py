from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QTableWidgetItem, QHBoxLayout, QSizePolicy
import sys
from PyQt6.QtSql import QSqlDatabase,QSqlQuery

from mark_manager import Ui_Form

class MarkManager(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.new_save.clicked.connect(self.add_marks)

        self.edit_save.clicked.connect(self.save_edit)

        self.connect_database()
        self.create_table()

        self.fetch_and_populate_table()

    def connect_database(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('./MarksManager/studentMarks.db')
        if db.open():
            print("Database connected successfully")
        else:
            print(db.lastError().text())

    def create_table(self):
        query = QSqlQuery()
        create_table = """
            CREATE TABLE IF NOT EXISTS studentDetails(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                full_name TEXT NOT NULL,
                admission_no TEXT NOT NULL,
                class TEXT NOT NULL,
                mathematics_marks INTEGER NOT NULL,
                english_marks INTEGER NOT NULL,
                kiswahili_marks INTEGER NOT NULL,
                science_marks INTEGER NOT NULL,
                social_studies_marks INTEGER NOT NULL,
                cre_marks INTEGER NOT NULL
            )
        """
        query.exec(create_table)

        if not query.exec(create_table):
            print(query.lastError().text())
            sys.exit(1)

    def add_marks(self):
        full_name = self.new_full_name.text()
        adm_no = self.new_adm_no.text()
        student_class = self.new_class.currentText()
        math_marks = self.new_math.text()
        eng_marks = self.new_eng.text()
        sci_marks = self.new_sci.text()
        kisw_marks = self.new_kisw.text()
        ss_marks = self.new_ss.text()
        cre_marks = self.new_cre.text()

        if not full_name or not adm_no or not student_class or not math_marks or not eng_marks or not kisw_marks or not sci_marks or not ss_marks or not cre_marks:
            print("All marks are required")
            return
        
        query = QSqlQuery()

        insert_query = "INSERT INTO studentDetails(full_name, admission_no, class, mathematics_marks, english_marks, kiswahili_marks, science_marks, social_studies_marks, cre_marks) VALUES(:full_name, :adm_no, :class, :math_marks, :eng_marks, :kisw_marks, :sci_marks, :ss_marks, :cre_marks)"

        query.prepare(insert_query)
        query.bindValue(':full_name', full_name)
        query.bindValue(':adm_no', adm_no)
        query.bindValue(':class', student_class)
        query.bindValue(':math_marks', math_marks)
        query.bindValue(':eng_marks', eng_marks)
        query.bindValue(':kisw_marks', kisw_marks)
        query.bindValue(':sci_marks', sci_marks)
        query.bindValue(':ss_marks', ss_marks)
        query.bindValue(':cre_marks', cre_marks)

        if query.exec():
            print('Data added')
            self.new_full_name.clear()
            self.new_adm_no.clear()
            self.new_class.clear()
            self.new_math.clear()
            self.new_eng.clear()
            self.new_sci.clear()
            self.new_kisw.clear()
            self.new_ss.clear()
            self.new_cre.clear()
            self.fetch_and_populate_table()
            self.stackedWidget.setCurrentIndex(1)
        else:
            print(query.lastError().text())

    def fetch_and_populate_table(self):
        """Fetch data from the database and populate the QTableWidget."""
        query = QSqlQuery("SELECT * FROM studentDetails")

        self.tableWidget.setRowCount(0)  # Clear existing rows
        row = 0
        while query.next():
            self.tableWidget.insertRow(row)

            # Loop through each column and populate it with data
            for col in range(10):  # 10 columns excluding the action button
                item = QTableWidgetItem(str(query.value(col)))
                self.tableWidget.setItem(row, col, item)
            
            # Create a QWidget container for buttons
            action_widget = QWidget()
            action_layout = QHBoxLayout(action_widget)  # Horizontal layout for buttons
            action_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
            action_layout.setSpacing(10)  # Add spacing between buttons
            
            # Create "Edit" and "Remove" buttons
            edit_button = QPushButton("Edit")
            remove_button = QPushButton("Remove")
            remove_button.setStyleSheet("background-color: red;")

            # Set a fixed width for buttons
            edit_button.setFixedWidth(80)
            remove_button.setFixedWidth(100)

            # Make buttons expand properly
            edit_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            remove_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

            # Connect the edit button to an action
            edit_button.clicked.connect(lambda _, id=query.value(0): self.edit_student(id))

            # Add buttons to layout
            action_layout.addWidget(edit_button)
            action_layout.addWidget(remove_button)

            # Set the container widget inside the table
            self.tableWidget.setCellWidget(row, 10, action_widget)

            row += 1

    def edit_student(self, id):
        """Populate edit fields when Edit button is clicked, fetching data from the database"""
        
        self.edit_id = id

        # Fetch data from the database
        query = QSqlQuery()
        query.prepare("SELECT full_name, admission_no, class, mathematics_marks, "
                    "english_marks, kiswahili_marks, science_marks, social_studies_marks, cre_marks "
                    "FROM studentDetails WHERE id = :id")
        query.bindValue(":id", self.edit_id)

        if query.exec() and query.next():  # Execute query and check if data is found
            self.edit_full_name.setText(query.value(0))
            self.edit_adm_no.setText(query.value(1))
            self.edit_class.setCurrentText(query.value(2))
            self.edit_math.setValue(int(query.value(3)))
            self.edit_eng.setValue(int(query.value(4)))
            self.edit_kisw.setValue(int(query.value(5)))
            self.edit_sci.setValue(int(query.value(6)))
            self.edit_ss.setValue(int(query.value(7)))
            self.edit_cre.setValue(int(query.value(8)))

            self.stackedWidget.setCurrentIndex(2)  # Switch to edit page
        else:
            print("Error fetching student record:", query.lastError().text())

    def save_edit(self):
        """Save the updated student details back to the database"""
        query = QSqlQuery()
        query.prepare("""
            UPDATE studentDetails SET 
                full_name = :full_name,
                admission_no = :admission_no,
                class = :class,
                mathematics_marks = :math_marks,
                english_marks = :eng_marks,
                kiswahili_marks = :kisw_marks,
                science_marks = :sci_marks,
                social_studies_marks = :ss_marks,
                cre_marks = :cre_marks
            WHERE id = :id
        """)

        query.bindValue(":id", self.edit_id)
        query.bindValue(":full_name", self.edit_full_name.text())
        query.bindValue(":admission_no", self.edit_adm_no.text())
        query.bindValue(":class", self.edit_class.currentText())
        query.bindValue(":math_marks", self.edit_math.value())
        query.bindValue(":eng_marks", self.edit_eng.value())
        query.bindValue(":kisw_marks", self.edit_kisw.value())
        query.bindValue(":sci_marks", self.edit_sci.value())
        query.bindValue(":ss_marks", self.edit_ss.value())
        query.bindValue(":cre_marks", self.edit_cre.value())

        if query.exec():
            print("Data updated successfully")
            self.fetch_and_populate_table()  # Refresh table data
            self.stackedWidget.setCurrentIndex(1)  # Switch back to main page
        else:
            print("Error updating record:", query.lastError().text())


app = QApplication(sys.argv)
notepad = MarkManager()
sys.exit(app.exec())