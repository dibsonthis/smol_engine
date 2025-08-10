import pyglet

type Window = pyglet.window.BaseWindow

class Renderer:

    def create_window(self, width: int = 1600, height: int = 1600, caption: str = "Engine Window", resizable: bool = True) -> pyglet.window.BaseWindow:
        """Create and return a Pyglet window."""
        return pyglet.window.Window(width=width, height=height, caption=caption, resizable=resizable)

    def draw_line(self, x1: float, y1: float, x2: float, y2: float, thickness: int = 2, color: tuple = (255, 255, 255)):
        """Draw a line on the window."""
        line = pyglet.shapes.Line(x1, y1, x2, y2, thickness=thickness, color=color)
        line.draw()

    def draw_rectangle(self, x: float, y: float, width: float, height: float, color: tuple = (255, 255, 255)):
        """Draw a rectangle on the window."""
        rectangle = pyglet.shapes.Rectangle(x, y, width, height, color=color)
        rectangle.draw()

    def draw_circle(self, x: float, y: float, radius: float, color: tuple = (255, 255, 255)):
        """Draw a circle on the window."""
        circle = pyglet.shapes.Circle(x, y, radius, color=color)
        circle.draw()