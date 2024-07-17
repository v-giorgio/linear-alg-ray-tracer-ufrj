import numpy as np

class Vector(np.ndarray):
    def __new__(cls, x, y, z):
        return np.asarray([x, y, z]).view(cls)
    
    def normalize(self):
        return self / np.linalg.norm(self)
    
    def reflected(self, axis):
        return self - 2 * np.dot(self, axis) * axis