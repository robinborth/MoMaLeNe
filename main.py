import sys
import signal
from PySide6.QtWidgets import QApplication
from lib.canvas import Canvas
from lib.simulator import Simulator
from lib.renderer import Renderer


def main():
    # settings
    width = 600
    height = 600
    fps = 90

    # create the application
    app = QApplication(sys.argv)

    def signal_handler(sig, frame):
        print("You pressed Ctrl+C")
        sys.exit(app.exit())

    def loop():
        nonlocal canvas
        nonlocal simulator
        nonlocal renderer
        state = simulator.step()
        img = renderer.render(state=state)
        canvas.render(data=img)

    # create simulation
    simulator = Simulator()

    # create renderer
    renderer = Renderer(width=width, height=height)

    # create canvas
    canvas = Canvas(
        width=width,
        height=height,
        fps=fps,
        loop=loop,
    )
    canvas.show()

    # close application on Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    # close the application
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
