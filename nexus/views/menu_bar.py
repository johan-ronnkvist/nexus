from PySide6.QtWidgets import QMenuBar, QMenu

from nexus.actions.quit import QuitAction


class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._file = self.addMenu("File")
        self._edit = self.addMenu("Edit")
        self._view = self.addMenu("View")
        self._help = self.addMenu("Help")

        self._configure_file()

    def _configure_file(self):
        self.file.addAction(QuitAction(self))
        pass

    @property
    def file(self) -> QMenu:
        return self._file

    @property
    def edit(self) -> QMenu:
        return self._edit

    @property
    def view(self) -> QMenu:
        return self._view

    @property
    def help(self) -> QMenu:
        return self._help
