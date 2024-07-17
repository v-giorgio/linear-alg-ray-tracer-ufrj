import numpy as np
from vector import Vector
from light import Light
from sphere import Sphere
from scene import Scene

file_name = 'another_sample'

# Altere a posição do espectador aqui:
camera = Vector(0, 0, 1)

# Altere a posição da fonte luminosa aqui:
light = Light(Vector(5, 5, 5), np.array([1, 1, 1]), np.array([1, 1, 1]), np.array([1, 1, 1]))

# Adicione objetos na imagem aqui:
objects = [
    Sphere(Vector(-0.2, 0, -1), 0.7, np.array([1, 0.5, 0]), np.array([0.1, 0, 0]), np.array([1, 1, 1]), 100, 0.5),
    Sphere(Vector(0.1, -0.3, 0), 0.1, np.array([0.1, 0, 0.1]), np.array([0.7, 0, 0.7]), np.array([1, 1, 1]), 100, 0.5),
    Sphere(Vector(-0.3, 0, 0), 0.15, np.array([0, 0.1, 0]), np.array([0, 0.6, 0]), np.array([1, 1, 1]), 100, 0.5),
    Sphere(Vector(0.1, -9000, 0), 9000 - 0.7, np.array([0.1, 0.1, 0.1]), np.array([0.6, 0.6, 0.6]), np.array([1, 1, 1]), 100, 0.5)
]
scene = Scene(camera, objects, light)

# Altere aqui para alterar as dimensões da imagem:
scene.render(1000, 1000, 3, file_name)
