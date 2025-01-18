import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QMenuBar, QLineEdit, QMessageBox, QComboBox
from PyQt5.QtCore import Qt
import math_tutoring_imports as mti
from sqlalchemy.engine import create_engine, Engine

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
    """This window is for entering in new records to the database."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.build_widgets()
        self.build_layout()

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
        layout = QHBoxLayout()

        layout.addWidget(self.record_label)
        layout.addWidget(self.options)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def assign_functions(self) -> None:
        """Assigns functionality to the widgets."""
        self.options.currentIndexChanged.connect(self.test_func)

    # Functions
    def test_func(self):
        print("Hello")

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
        try:
            engine = create_engine(f"postgresql+psycopg2://{user_db}:{password_db}@{host_db}:{port_db}/{name_db}")
            database_engine = engine
            msg = QMessageBox()
            msg.setText("Connection Successful")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        except Exception as e:
            msg = QMessageBox()
            msg.setText("Connection Failed")
            msg.setStandardButtons(QMessageBox.Retry)
            msg.setDetailedText(str(e))
            msg.exec_()

def main():
    database_engine = None

    app = QApplication([])

    window = HomeWindow()
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()

