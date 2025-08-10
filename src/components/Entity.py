import math
import random
import pyglet
from engine.engine import Component, RigidBody

class Entity(Component):
    def __init__(self, x: float = 0, y: float = 0):
        super().__init__()
        self.transform.x = x
        self.transform.y = y
        self.speed = 500
        self.target = [x, y]
        self.color = (0, 150, 0)  # Default color

    def set_random_target(self, min_distance=500):
        while True:
            tx = random.randint(0, self.engine.window.width)
            ty = random.randint(0, self.engine.window.height)
            dist = math.dist((self.transform.x, self.transform.y), (tx, ty))
            if dist >= min_distance:
                self.target = [tx, ty]
                break

    def init(self):
        print(f"Initializing Entity - {self.id}")

    def update(self, delta_time):
        # If close to target, pick a new one
        if math.dist([self.transform.x, self.transform.y], self.target) < 20:
            self.set_random_target()

        # Move toward target
        dx = self.target[0] - self.transform.x
        dy = self.target[1] - self.transform.y
        dist = math.hypot(dx, dy)
        if dist > 0:
            self.transform.x += (dx / dist) * self.speed * delta_time
            self.transform.y += (dy / dist) * self.speed * delta_time

        # Normalize position to 0-1
        norm_x = self.transform.x / self.engine.window.width
        norm_y = self.transform.y / self.engine.window.height

        # Map normalized x,y to RGB 0-255
        r = int(norm_x * 255)
        g = int(norm_y * 255)
        b = 255 - r  # Just an example, invert red for blue channel

        self.color = (r, g, b)

    def destroy(self):  
        print(f"Destroying Entity - {self.id}")

    def on_key_down_global(self, key):
        print(f"Entity Key Down: {key} - {self.id}")

    def on_mouse_click(self, x, y, button, modifiers):
        if x < self.transform.x + 50 and x > self.transform.x - 50 and \
           y < self.transform.y + 50 and y > self.transform.y - 50:
            print(f"Entity Clicked: {self.id} at ({x}, {y}) with button {button} pressed")
            self.destroy()

    # def on_mouse_motion(self, x, y, dx, dy):
    #     self.transform.x = x
    #     self.transform.y = y

    def render(self, window, renderer):
        renderer.draw_circle(self.transform.x, self.transform.y, self.transform.x / 4, color=self.color)
