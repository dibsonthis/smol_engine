import time
import uuid
from pynput import keyboard, mouse
from .renderer import Renderer, Window

class Transform:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return f"Transform(x: {self.x}, y: {self.y}, z: {self.z})"
    
class RigidBody:
    def __init__(self, mass: float = 1.0, velocity: Transform = Transform()):
        self.mass = mass
        self.velocity = velocity

    def __repr__(self):
        return f"RigidBody(mass: {self.mass}, velocity: {self.velocity})"

class Component:
    def __init__(self):
        self.active = True
        self.id = uuid.uuid4()
        self.transform = Transform()
        self.scale = Transform(1, 1, 1)
        self.rotation = Transform()
        self.rigid_body = None
        self.data = {}
        self.engine: Engine = None

    def init(self):
        pass

    def update(self, delta_time: float):
        pass

    def render(self, window: Window, renderer: Renderer):
        pass

    def destroy(self):
        pass

    def __destroy__(self):
        pass

    def on_key_down_global(self, key: str):
        pass

    def on_key_up_global(self, key: str):
        pass

    def on_mouse_click_global(self, x: float, y: float, button: int, pressed: bool):
        pass

    def on_mouse_motion_global(self, x: float, y: float):
        pass

    def on_mouse_scroll_global(self, x: float, y: float, dx: float, dy: float):
        pass

    # Window event handlers

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        pass

    def on_mouse_click(self, x: float, y: float, button: int, modifiers: int):
        pass

class Engine:
    def __init__(self):
        self.renderer = Renderer()
        self.running = False
        self.sleep = 1
        self.components: list[Component] = []
        self.window: Window = self.renderer.create_window()
        self.keyboard_listener = keyboard.Listener(on_press=self.on_key_down_global, on_release=self.on_key_up_global)
        self.mouse_listener = mouse.Listener(
            on_click=self.on_mouse_click_global,
            on_move=self.on_mouse_motion_global,
            on_scroll=self.on_mouse_scroll_global
        )
        # Register class methods as event handlers
        self.window.push_handlers(self)

        self.previous_time = time.time()
        self.delta_time = 0

    def start(self):
        self.running = True

        self.keyboard_listener.start()
        self.mouse_listener.start()

        for component in self.components:
            component.init()
        while self.running:
            current_time = time.time()
            self.delta_time = current_time - self.previous_time
            self.previous_time = current_time 

            if self.window.has_exit:
                self.stop()
                break
            for component in self.components:
                component.update(self.delta_time)

            self.window.dispatch_events()  # process OS/window events
            self.window.clear()

            for component in self.components:
                component.render(self.window, self.renderer)

            self.window.flip()  # swap back/front buffers
            time.sleep(1/60)  # simulate ~60 FPS

    def stop(self):
        self.running = False
        for component in self.components:
            component.__destroy__()
        self.components.clear()

        try:
            self.mouse_listener.stop()
            self.mouse_listener.join()
            self.keyboard_listener.stop()
            self.keyboard_listener.join()
        except:
            pass

    def register_component(self, component):
        if isinstance(component, Component):
            # Monkey patch removing the component when destroy is called
            _destroy = component.destroy
            def destroy_patch():
                _destroy()
                self.unregister_component(component)
            component.destroy = destroy_patch
            component.__destroy__ = _destroy

            # Add a reference to the engine
            component.engine = self

            self.components.append(component)

    def unregister_component(self, component):
        if component in self.components:
            self.components.remove(component)

    # Keyboard event handlers

    def on_key_down_global(self, key):
        if key == keyboard.Key.esc:
            self.stop()
        for component in self.components:
            component.on_key_down_global(key)

    def on_key_up_global(self, key):
        for component in self.components:
            component.on_key_up_global(key)

    # Mouse event handlers

    def on_mouse_click_global(self, x, y, button, pressed):
        for component in self.components:
            component.on_mouse_click_global(x, y, button, pressed)

    def on_mouse_motion_global(self, x, y):
        for component in self.components:
            component.on_mouse_motion_global(x, y)

    def on_mouse_scroll_global(self, x, y, dx, dy):
        for component in self.components:
            component.on_mouse_scroll_global(x, y, dx, dy)

    # Window event handlers

    def on_mouse_motion(self, x, y, dx, dy):
        for component in self.components:
            component.on_mouse_motion(x, y, dx, dy)

    def on_mouse_press(self, x, y, button, modifiers):
        for component in self.components:
            component.on_mouse_click(x, y, button, modifiers)
    