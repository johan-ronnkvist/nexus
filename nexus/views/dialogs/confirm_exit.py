from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout


class ConfirmExitDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Confirm Exit")
        layout = QVBoxLayout()

        # Add a label with the warning message
        self.message_label = QLabel("You have unsaved changes. Do you want to exit without saving?")
        layout.addWidget(self.message_label)

        # Create buttons
        self.save_and_exit_button = QPushButton("Save and Exit")
        self.exit_without_saving_button = QPushButton("Exit without Saving")
        self.cancel_button = QPushButton("Cancel")

        layout.addWidget(self.save_and_exit_button)
        layout.addWidget(self.exit_without_saving_button)
        layout.addWidget(self.cancel_button)

        # Connect buttons to slots
        self.save_and_exit_button.clicked.connect(self.on_save_and_exit)
        self.exit_without_saving_button.clicked.connect(self.on_exit_without_saving)
        self.cancel_button.clicked.connect(self.reject)

        self.setLayout(layout)

    def on_save_and_exit(self):
        # Add your save logic here if needed
        # For this example, we'll just accept the dialog
        self.accept()

    def on_exit_without_saving(self):
        # This method can be used to set a flag or perform any other necessary task
        # before actually exiting without saving. For now, we're just closing the dialog.
        self.accept()
