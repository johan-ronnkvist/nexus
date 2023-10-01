from PySide6.QtWidgets import QGraphicsView


class SceneView(QGraphicsView):
    def __int__(self, parent=None):
        super().__init__(parent)
