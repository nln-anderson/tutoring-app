from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableView, QDialog, QVBoxLayout, QPushButton, QHBoxLayout
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

class TableWindow(QMainWindow):
    """Window containing one table from a valid database connection"""
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

class PickListDialog(QDialog):
    """This is a proper picklist dialog."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Picklist")
        self.resize(1000, 500)
        self.selected_row = None

        self.create_QTableView()
        self.build_buttons()
        self.build_layout()

    def create_QTableView(self) -> None:
        self.table_view = QTableView()
        self.model = QSqlTableModel()
        self.model.setTable("students")
        self.table_view.setModel(self.model)
        self.model.select()

        self.table_view.setSelectionBehavior(QTableView.SelectRows)
        self.table_view.setSelectionMode(QTableView.SingleSelection)
        self.table_view.resizeColumnsToContents()
        self.table_view.setSortingEnabled(True)

    def build_buttons(self) -> None:
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")

        self.ok_button.clicked.connect(self.accept_selection)
        self.cancel_button.clicked.connect(self.reject)

    def build_layout(self) -> None:
        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def accept_selection(self):
        selected_indexes = self.table_view.selectionModel().selectedRows()
        print(selected_indexes[0].row())
        if selected_indexes:
            selected_row = selected_indexes[0].row()
            self.selected_row = [
                self.model.data(self.model.index(selected_row, col))
                for col in range(self.model.columnCount())
            ]
        self.accept()
        self.get_selected_row()

    def get_selected_row(self):
        print(self.selected_row)
        return self.selected_row

if __name__ == "__main__":
    app = QApplication([])
    database_test()
    window = PickListDialog()
    window.show()
    app.exec_()