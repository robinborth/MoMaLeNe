import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QImage, QPainter, QPaintEvent
from PySide6.QtCore import QTimer


class Canvas(QMainWindow):
    def __init__(
        self,
        title: str = "MoMaLeNe",
        width: int = 800,
        height: int = 600,
        fps: int = 30,
        loop: None = None,
    ):
        super().__init__()
        self.setWindowTitle(title)
        # Get the size of the window
        self.setFixedSize(width, height)
        # Center the window on the screen
        self.center()
        self.data = np.zeros((height, width, 3), dtype=np.uint8)

        # Set up a QTimer to control the FPS and automatic movement
        self.frame_count = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(loop)
        self.timer.start(int(1000 / fps))

    def center(self):
        # Get the screen's dimensions
        screen = QApplication.primaryScreen()  # Get the primary screen
        screen_geometry = screen.geometry()  # Get the geometry of the screen

        # Calculate the center point
        center_x = screen_geometry.width() // 2 - self.width() // 2
        center_y = screen_geometry.height() // 2 - self.height() // 2

        # Set the position of the window
        self.setGeometry(center_x, center_y, self.width(), self.height())

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)

        # Convert the NumPy array to QImage
        height, width, channel = self.data.shape
        bytes_per_line = 3 * width
        q_image = QImage(
            self.data.data,
            width,
            height,
            bytes_per_line,
            QImage.Format_RGB888,  # type: ignore
        )

        # Draw the image at the current position (x, y)
        painter.drawImage(0, 0, q_image)
        print(f"{self.frame_count=}")
        self.frame_count += 1

    def render(self, data):
        self.data = data
        self.update()
