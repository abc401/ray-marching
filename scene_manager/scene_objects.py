from pygame import Vector3, Color, Vector2
from abc import ABC, abstractmethod
from colors import *


class RayMarchingObject(ABC):
    def __init__(self, color: Color = RED) -> None:
        super().__init__()
        self.color = color
    
    @abstractmethod
    def sdf(self, point: Vector3) -> float:
        pass


class Circle(RayMarchingObject):
    def __init__(self, center: Vector3, radius: float, color: Color = RED) -> None:
        super().__init__(color)
        self.center = Vector3(center)
        self.radius = radius
    
    def sdf(self, point: Vector3) -> float:
        return (self.center - point).magnitude() - self.radius


class IntersectionObject(RayMarchingObject):
    def __init__(self, *scene_objects: RayMarchingObject) -> None:
        super().__init__()
        self.scene_objects = scene_objects
    
    def sdf(self, point: Vector3) -> float:
        return max([scene_object.sdf(point) for scene_object in self.scene_objects])