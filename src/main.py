import sys
import os

# Add the parent directory of 'engine' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from components.Entity import Entity
from components.Scene import Scene

from engine.engine import Engine

engine = Engine()

scene = Scene()
engine.register_component(scene)

# engine.register_component(Entity(100, 100))

for i in range(1, 6):
    engine.register_component(Entity(i * 100, i * 100))

engine.sleep = 1
engine.start()