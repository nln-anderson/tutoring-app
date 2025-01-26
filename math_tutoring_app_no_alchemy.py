import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QMenuBar, QLineEdit, QMessageBox, QComboBox, QTableView, QDialog
from PyQt5.QtCore import Qt
import math_tutoring_imports as mti
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
import picklist_imports as pi

class HomeWindow(QMainWindow):
    """Child class of the main window object."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setting any instance variables
        self.setWindowTitle("Nolan's Math Tutoring")

        # Calling the add_widgets function
        self.add_widgets()
        self.create_layout()
        self.assign_functions()

    def add_widgets(self) -> None:
        """This function adds the widgets to our window object."""
        # First button
        button = QPushButton("Add Sessions/Records")
        self.view_button = button

        # Second Button
        button2 = QPushButton("View and Analyze Records")
        self.button2 = button2

        # Menubar
        self.menubar = QMenuBar(self)

    def create_layout(self) -> None:
        """Creates the layout and addes the widgets"""
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.view_button)
        self.layout.addWidget(self.button2)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        # Menubar stuff
        self.setMenuBar(self.menubar)
        self.file_menu = self.menubar.addMenu("File")
        self.options_menu = self.menubar.addMenu("Options")

    def assign_functions(self) -> None:
        """Assigns the functions to widgets"""
        db_action = self.file_menu.addAction("Connect to Database")
        db_action.triggered.connect(self.db_function)

        self.view_button.clicked.connect(self.create_add_insert_window)

    # Functions
    def db_function(self):
        self.db_window = DB_Window()
        self.db_window.show()
    
    def create_add_insert_window(self) -> None:
        self.insert_window = InsertWindow()
        self.insert_window.show()

class InsertWindow(QMainWindow):
    # Instance vars
    row_id: int # ID of selected row from picklist

    """This window is for entering in new records to the database."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.build_widgets()
        self.build_layout()
        self.assign_functions()

    def build_widgets(self) -> None:
        """Creates all the widgets used by this window"""
        self.record_label = QLabel()
        self.record_label.setText("Record Type:")
        self.options = QComboBox()
        self.options.addItem("")
        self.options.addItem("Student")
        self.options.addItem("Session")
    
    def build_layout(self) -> None:
        """Builds the layout of the window"""
        # Overarching layout
        self.parent_layout = QVBoxLayout()

        # Layout for the top buttons
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.record_label)
        top_layout.addWidget(self.options)

        # Layout for field entries. This will be edited when a subsection is selected.
        self.field_layout = QVBoxLayout()
        fields_label = QLabel(text="Fields:")
        self.field_layout.addWidget(fields_label)

        # Layout for the buttons at the bottom
        self.button_layout = QHBoxLayout()
        self.accept_button = QPushButton(text="Accept")
        self.cancel_button = QPushButton(text="Cancel")
        self.button_layout.addWidget(self.accept_button)
        self.button_layout.addWidget(self.cancel_button)

        # Adding the layouts to the parent
        self.parent_layout.addLayout(top_layout)
        self.parent_layout.addLayout(self.field_layout)
        self.parent_layout.addLayout(self.button_layout)
        self.parent_widget = QWidget()
        self.parent_widget.setLayout(self.parent_layout)
        self.setCentralWidget(self.parent_widget)

    def assign_functions(self) -> None:
        """Assigns functionality to the widgets."""
        self.options.currentIndexChanged.connect(self.options_handler)

    # Functions
    def student_records(self) -> None:
        """This sets up the window for student record entry"""
        self.toolbar = mti.CustomToolbar()
        self.addToolBar(self.toolbar)
        self.toolbar.view_picklist.triggered.connect(self.open_picklist_students)

        self.first_name_LI = mti.LabeledInput("First Name:")
        self.last_name_LI = mti.LabeledInput("Last Name:")
        self.math_level_LI = mti.LabeledInput("Math Level:")
        self.grade_level_LI = mti.LabeledInput("Grade Level:")
        self.school_LI = mti.LabeledInput("School:")
        
        self.field_layout.addWidget(self.first_name_LI)
        self.field_layout.addWidget(self.last_name_LI)
        self.field_layout.addWidget(self.math_level_LI)
        self.field_layout.addWidget(self.grade_level_LI)
        self.field_layout.addWidget(self.school_LI)

    def options_handler(self, index):
        """This guides the selection to execute the proper function to update the window."""
        if index == 1:
            self.student_records()
        elif index == 0:
            pass
        if index ==2:
            self.sessions_records()

    def open_picklist_students(self) -> None:
        """Opens a dialog box and returns the ID of selected row."""
        pick_list = pi.PickListDialog(table_name="students")
        if pick_list.exec_() == QDialog.Accepted:
                self.row_id = pick_list.get_selected_row_id()

class DB_Window(QMainWindow):
    """This class represents the window for the database connection option."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Connect to Database")
        self.resize(300, 200)

        self.build_widgets()
        self.build_layout()
        self.assign_functions()

    def build_widgets(self) -> None:
        """Creates all the widgets of this window."""
        self.db_name_widget = mti.LabeledInput("Database Name:")
        self.db_host_widget = mti.LabeledInput("DB Host:")
        self.db_port_widget = mti.LabeledInput("DB Port:")
        self.db_user_widget = mti.LabeledInput("DB Username:")
        self.db_password_widget = mti.LabeledInput("DB Password:")
        self.db_password_widget.text_field.setEchoMode(QLineEdit.EchoMode.Password)

        self.connect_button = QPushButton("Connect to Database")

    def build_layout(self) -> None:
        """Builds the layout of the database window"""
        central_widget = QWidget()

        # Adding the widgets to the layout
        layout = QVBoxLayout()
        layout.addWidget(self.db_name_widget)
        layout.addWidget(self.db_host_widget)
        layout.addWidget(self.db_port_widget)
        layout.addWidget(self.db_user_widget)
        layout.addWidget(self.db_password_widget)
        layout.addWidget(self.connect_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def assign_functions(self) -> None:
        """Assigns the functions to the signals."""
        self.connect_button.clicked.connect(self.connect_to_database)

    # Functions
    def connect_to_database(self) -> None:
        """This gathers the inputs for the database connection and tries to connect."""
        # Gather the fields
        name_db = self.db_name_widget.get_text()
        host_db = self.db_host_widget.get_text()
        port_db = self.db_port_widget.get_text()
        user_db = self.db_user_widget.get_text()
        password_db = self.db_password_widget.get_text()

        # Test connection
        
        connection = QSqlDatabase.addDatabase("QPSQL")
        connection.setDatabaseName(name_db)
        connection.setHostName(host_db)
        connection.setPort(int(port_db))
        connection.open(user_db, password_db)
        database_engine = connection
        
        if connection.isOpen():
            msg = QMessageBox()
            msg.setText("Connection Successful")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setText("Connection Failed")
            msg.setStandardButtons(QMessageBox.Retry)
            msg.setDetailedText("Something went wrong")
            msg.exec_()

def main():
    database_engine = None

    app = QApplication([])

    window = HomeWindow()
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()

