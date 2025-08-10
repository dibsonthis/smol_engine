import pyglet
from engine.engine import Component, RigidBody

class Entity(Component):
    def __init__(self, x: float = 0, y: float = 0):
        super().__init__()
        self.transform.x = x
        self.transform.y = y
        self.rigid_body = RigidBody(50)

    def init(self):
        print(f"Initializing Entity - {self.id}")

    def update(self):
        pass

    def destroy(self):  
        print(f"Destroying Entity - {self.id}")

    def on_key_down_global(self, key):
        print(f"Entity Key Down: {key} - {self.id}")

    # def on_mouse_click_global(self, x, y, button, pressed):
    #     if x < self.transform.x + 50 and x > self.transform.x - 50 and \
    #        y < self.transform.y + 50 and y > self.transform.y - 50:
    #         print(f"Entity Clicked: {self.id} at ({x}, {y}) with button {button} {'pressed' if pressed else 'released'}")
    #         self.destroy()

    def on_mouse_click(self, x, y, button, modifiers):
        if x < self.transform.x + 50 and x > self.transform.x - 50 and \
           y < self.transform.y + 50 and y > self.transform.y - 50:
            print(f"Entity Clicked: {self.id} at ({x}, {y}) with button {button} pressed")
            self.destroy()

    # def on_mouse_motion(self, x, y, dx, dy):
    #     self.transform.x = x
    #     self.transform.y = y

    def render(self, window, renderer):
        renderer.draw_circle(self.transform.x, self.transform.y, self.transform.x / 4, color=(0, 150, 0))
