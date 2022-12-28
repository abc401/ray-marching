from scene_manager.scene_objects import RayMarchingObject


class Scene:
    def __init__(self, *scene_objects: RayMarchingObject) -> None:
        self.scene_objects: list[RayMarchingObject] = scene_objects
    
    def append(self, scene_object: RayMarchingObject):
        self.scene_objects.append(scene_object)