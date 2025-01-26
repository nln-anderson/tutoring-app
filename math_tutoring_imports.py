from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QToolBar, QAction, QMainWindow, QApplication, QTableView, QPushButton, QVBoxLayout, QDialog
from PyQt5.QtGui import QIcon, QStandardItem, QStandardItemModel
from PyQt5.QtCore import QSize, QAbstractTableModel
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker

class LabeledInput(QWidget):
    def __init__(self, label_text, placeholder_text="", parent=None):
        super().__init__(parent)

        # Create label and text field
        self.label = QLabel(label_text)
        self.text_field = QLineEdit()
        self.text_field.setPlaceholderText(placeholder_text)

        # Layout for the widget
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_field)

        # Set the layout
        self.setLayout(layout)

    def get_text(self) -> str:
        return str(self.text_field.text())

    def set_text(self, text):
        self.text_field.setText(text)

class TestWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CustomToolbar_test(QToolBar):
    """Custom toolbar for navigating."""
    # Instance variables
    view_picklist: QAction
    previous: QAction
    next: QAction 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setIconSize(QSize(32,32))
        self.setup_actions()

    def setup_actions(self) -> None:
        """Sets up all the actions for this toolbar."""
        self.view_picklist = QAction(QIcon("binoculars.png"), "View All", self)
        self.view_picklist.triggered.connect(self.functionality_testing)
        self.addAction(self.view_picklist)

        self.previous = QAction("<", self)
        self.addAction(self.previous)

        self.next = QAction(">", self)
        self.addAction(self.next)

    def functionality_testing(self) -> None:
        print("Hello")

class CustomToolbar(QToolBar):
    """Custom toolbar for navigating."""
    # Instance variables
    view_picklist: QAction
    previous: QAction
    next: QAction 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setIconSize(QSize(32,32))
        self.setup_actions()

    def setup_actions(self) -> None:
        """Sets up all the actions for this toolbar."""
        self.view_picklist = QAction(QIcon("binoculars.png"), "View All", self)
        self.addAction(self.view_picklist)

        self.previous = QAction("<", self)
        self.addAction(self.previous)

        self.next = QAction(">", self)
        self.addAction(self.next)


if __name__ == "__main__":
    app = QApplication([])

    window = TestWindow()
    toolbar = CustomToolbar_test()
    window.addToolBar(toolbar)

    window.show()
    app.exec_()