from engine.engine import Component


class Scene(Component):
    def render(self, window, renderer):
        cell_size = window.width // 5

        # Vertical lines
        for i in range(6):
            x = i * cell_size
            renderer.draw_line(x, 0, x, window.height, thickness=2, color=(255, 255, 255))

        # Horizontal lines
        for i in range(6):
            y = i * cell_size
            renderer.draw_line(0, y, window.width, y, thickness=2, color=(255, 255, 255))