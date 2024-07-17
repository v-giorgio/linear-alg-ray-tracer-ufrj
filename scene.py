import numpy as np
import matplotlib.pyplot as plt

from vector import Vector
from ray import Ray

class Scene:
    def __init__(self, camera, objects, light):
        self.camera = camera
        self.objects = objects
        self.light = light

    def get_closest_intersected_obj(self, ray):
        distances = [obj.intersect(ray) for obj in self.objects]
        nearest_object = None
        min_distance = np.inf
        for index, distance in enumerate(distances):
            if distance and distance < min_distance:
                min_distance = distance
                nearest_object = self.objects[index]
        return nearest_object, min_distance

    def render(self, width, height, max_depth, file_name):
        ratio = float(width) / height
        screen = (-1, 1 / ratio, 1, -1 / ratio)
        image = np.zeros((height, width, 3))
        for i, y in enumerate(np.linspace(screen[1], screen[3], height)):
            for j, x in enumerate(np.linspace(screen[0], screen[2], width)):
                pixel = Vector(x, y, 0)
                ray = Ray(self.camera, pixel - self.camera)
                color = np.zeros([(3)])
                reflection = 1
                for _ in range(max_depth):
                    nearest_object, min_distance = self.get_closest_intersected_obj(ray)
                    if nearest_object is None:
                        break
                    intersection = ray.origin + min_distance * ray.direction
                    normal_to_surface = (intersection - nearest_object.center).normalize()
                    shifted_point = intersection + 1e-5 * normal_to_surface
                    intersection_to_light = (self.light.position - shifted_point).normalize()
                    _, min_distance = self.get_closest_intersected_obj(Ray(shifted_point, intersection_to_light))
                    intersection_to_light_distance = np.linalg.norm(self.light.position - intersection)
                    is_shadowed = min_distance < intersection_to_light_distance
                    if is_shadowed:
                        break
                    illumination = np.zeros((3))
                    illumination += nearest_object.ambient * self.light.ambient
                    illumination += nearest_object.diffuse * self.light.diffuse * np.dot(intersection_to_light, normal_to_surface)
                    intersection_to_camera = (self.camera - intersection).normalize()
                    H = (intersection_to_light + intersection_to_camera).normalize()
                    illumination += nearest_object.specular * self.light.specular * np.dot(normal_to_surface, H) ** (nearest_object.shininess / 4)
                    color += reflection * illumination
                    reflection *= nearest_object.reflection
                    ray.origin = shifted_point
                    ray.direction = ray.direction.reflected(normal_to_surface)
                image[i, j] = np.clip(color, 0, 1)
            print("Progress: %d/%d" % (i + 1, height))

        plt.imsave(f'./asset/{file_name}.png', image)