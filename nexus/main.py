import logging
import sys

from PySide6.QtWidgets import QApplication

from nexus.views.main_window import MainWindow

_logger = logging.getLogger(__name__)

if __name__ == "__main__":
    _logger.debug("Starting Nexus")
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    exit_code = app.exec()
    _logger.debug(f"Exiting Nexus (exit code:{exit_code})")

    sys.exit(exit_code)
