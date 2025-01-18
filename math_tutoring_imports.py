from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout

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
