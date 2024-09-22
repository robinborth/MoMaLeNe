import sys
from PySide6.QtWidgets import QApplication
from lib.canvas import Canvas
from lib.simulator import SquareSimulator, ParticleSimulator
from lib.renderer import SquareRenderer, ParticleRenderer


def main():
    # settings
    width = 800
    height = 600
    fps = 90

    # create the application
    app = QApplication(sys.argv)

    def loop():
        nonlocal canvas
        nonlocal simulator
        nonlocal renderer
        state = simulator.step()
        img = renderer.render(state=state)
        canvas.render(data=img)

    # create simulation
    # simulator = SquareSimulator(init_x=0, init_y=0, size=100)
    simulator = ParticleSimulator()
    # create renderer
    renderer = ParticleRenderer(width=width, height=height)

    # create canvas
    canvas = Canvas(
        width=width,
        height=height,
        fps=fps,
        loop=loop,
    )
    canvas.show()

    # close the application
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
