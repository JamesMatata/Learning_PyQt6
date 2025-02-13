import sys
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtWidgets import QApplication

def create_database():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('example.db')
    if not db.open():
        print("Database Error: %s" % db.lastError().text())
        return False
    
    db.transaction()

    query = QSqlQuery()

    create_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """

    if not query.exec(create_query):
        print("Error in creating table: %s" % query.lastError().text())
        db.rollback()
        return False
    
    insert_query = """
        INSERT INTO users (name, email) VALUES
        ('John Doe', 'j@gmail.com'),
        ('Jane Doe', 'jofn@gmail.com')

    """

    if not query.exec(insert_query):
        print("Error in inserting data: %s" % query.lastError().text())
        db.rollback()
        return False
    

    db.commit()
    return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    if create_database():
        print("Database created successfully")
    sys.exit(app.exec())