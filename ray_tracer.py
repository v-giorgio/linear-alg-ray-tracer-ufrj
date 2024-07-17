import numpy as np
from vector import Vector
from light import Light
from sphere import Sphere
from scene import Scene

file_name = 'another_sample'

camera = Vector(0, 0, 1)
# light = Light(Vector(0, 0, 1), np.array([1, 1, 1]), np.array([1, 1, 1]), np.array([1, 1, 1]))
# objects = [
#     Sphere(Vector(0, 0, -1), 0.7, np.array([1, 0.5, 0]), np.array([1, 0.5, 0]), np.array([1, 1, 1]), 100, 0.5),  # Orange sphere
#     Sphere(Vector(0, -9000, 0), 9000 - 0.7, np.array([0.1, 0.05, 0]), np.array([0.15, 0.07, 0.03]), np.array([1, 1, 1]), 100, 0.5)  # Deep dark brown field
# ]

light = Light(Vector(5, 5, 5), np.array([1, 1, 1]), np.array([1, 1, 1]), np.array([1, 1, 1]))
objects = [
    Sphere(Vector(-0.2, 0, -1), 0.7, np.array([1, 0.5, 0]), np.array([0.1, 0, 0]), np.array([1, 1, 1]), 100, 0.5),
    Sphere(Vector(0.1, -0.3, 0), 0.1, np.array([0.1, 0, 0.1]), np.array([0.7, 0, 0.7]), np.array([1, 1, 1]), 100, 0.5),
    Sphere(Vector(-0.3, 0, 0), 0.15, np.array([0, 0.1, 0]), np.array([0, 0.6, 0]), np.array([1, 1, 1]), 100, 0.5),
    Sphere(Vector(0.1, -9000, 0), 9000 - 0.7, np.array([0.1, 0.1, 0.1]), np.array([0.6, 0.6, 0.6]), np.array([1, 1, 1]), 100, 0.5)
]

scene = Scene(camera, objects, light)

scene.render(1000, 1000, 3, file_name)
