from pygame import Vector2
from abc import ABC, abstractmethod


class RayMarchingObject(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def signed_distance(self, point: Vector2) -> float:
        pass


class Circle(RayMarchingObject):
    def __init__(self, center: Vector2, radius: float) -> None:
        super().__init__()
        self.center = center
        self.radius = radius
    
    def signed_distance(self, point: Vector2) -> float:
        return (self.center - point).magnitude()


class IntersectionObject(RayMarchingObject):
    def __init__(self, object1: RayMarchingObject, object2: RayMarchingObject) -> None:
        super().__init__()
        self.object1 = object1
        self.object2 = object2
    
    def signed_distance(self, point: Vector2) -> float:
        return max(
            self.object1.signed_distance(point),
            self.object2.signed_distance(point)
            )