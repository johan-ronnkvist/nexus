from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QMainWindow

from nexus.views.graphics_scene import QGraphicsView
from nexus.views.menu_bar import MenuBar
from nexus.views.status_bar import StatusBar


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nexus")
        self.setMinimumSize(800, 600)
        self.setMenuBar(MenuBar(self))
        self.setStatusBar(StatusBar(self))
        self.setCentralWidget(QGraphicsView())

    def _has_unsaved_changed(self) -> bool:
        return False

    def _discard_changes(self) -> bool:
        return True

    def closeEvent(self, event: QCloseEvent) -> None:
        if self._has_unsaved_changed():
            if not self._discard_changes():
                event.ignore()

        event.accept()
