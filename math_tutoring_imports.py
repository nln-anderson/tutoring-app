from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QToolBar
from PyQt5.QtGui import QIcon

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
    
class CustomToolbar(QToolBar):
    """Custom toolbar for navigating."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup_actions(self) -> None:
        """Sets up all the actions for this toolbar"""
        view_picklist = QLabel(QIcon("binoculars.png"), "View All", self)

if __name__ == "__main__":
    pass