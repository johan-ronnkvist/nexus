from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QAction


class QuitAction(QAction):
    def __init__(self, parent=None):
        super().__init__("Exit", parent)
        self.setShortcut("Ctrl+Q")
        self.setStatusTip("Exit the application")
        self.triggered.connect(self._on_triggered)

    def _on_triggered(self):
        QCoreApplication.instance().quit()
