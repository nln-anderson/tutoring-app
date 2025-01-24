from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableView
from PyQt5.QtCore import Qt

def database_test() -> None:
    # Setting up connection to database
    connection = QSqlDatabase.addDatabase("QPSQL")
    connection.setDatabaseName("postgres")
    connection.setHostName("localhost")

    # Opening the connection
    print(connection.open("postgres", "password123"))

    # Testing a query
    table_query = QSqlQuery()
    table_query.exec(
        """
        SELECT * FROM students
        """)
    while table_query.next() == True:
        print(table_query.value(1))  

class DatabaseWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Here is a table")
        self.resize(415, 200)

        # Set up the model
        self.model = QSqlTableModel()
        self.model.setTable("students")
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()

        # Set up the view
        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.resizeColumnsToContents()
        self.setCentralWidget(self.view)


if __name__ == "__main__":
    app = QApplication([])
    database_test()
    window = DatabaseWindow()
    window.show()
    app.exec_()