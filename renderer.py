from pygame import Surface, Vector3, Vector2
from scene_manager.scene import Scene
import pygame
import colors


class RayMarchingRenderer:
    def __init__(self, surface: Surface) -> None:
        self.surface = surface
        self.MAX_DIST = 1000
        self.HIT_DIST = 0.01
        # self.camera = Vector3(self.surface.get_width()/2, self.surface.get_height()/2, 0)
        self.camera = Vector3(0, 0, 0)
        self.zoom = 40
        self.MAX_STEPS = 100
    
    def step(self, _from: Vector3, scene: Scene):
        dist = scene.scene_objects[0].sdf(_from)
        color = scene.scene_objects[0].color
        for scene_object in scene.scene_objects:
            if scene_object.sdf(_from) < dist:
                dist = scene_object.sdf(_from)
                color = scene_object.color
        return dist, color
            
    def march(self, _from: Vector3, _theta: Vector3, scene: Scene):
        for i in range(self.MAX_STEPS):
            step_dist, color = self.step(_from, scene)
            _from += step_dist * _theta

            if step_dist < self.HIT_DIST or _from.magnitude()  > self.MAX_DIST:
                break
        return _from, color

    def render(self,
            #    _theta: Vector2, 
               scene: Scene):
        
        _from = Vector3(self.camera)
        for i in range(self.surface.get_width()):
            for j in range(self.surface.get_height()):
                # _from = Vector2(self.camera)
                _theta = (
                    Vector3(
                        i - self.surface.get_width()/2,
                        j - self.surface.get_height()/2,
                        self.zoom
                    ) - _from
                ).normalize()
                dist, color = self.march(_from.copy(), _theta, scene)
                if dist.magnitude() < self.MAX_DIST:
                    self.surface.set_at((i, j), color)
    # def render(self, _theta: Vector2, scene: Scene):
    #     self.surface.fill(colors.BLACK)
    #     _from = Vector2(self.camera)
    #     for _ in range(self.MAX_STEPS):
    #         step_dist, color = self.step(_from, scene)

    #         pygame.draw.circle(self.surface, colors.WHITE, _from, step_dist, 1)
    #         pygame.draw.line(self.surface, colors.WHITE, _from, _from+(step_dist * _theta))
    #         _from += step_dist * _theta
    #         if step_dist < self.HIT_DIST or _from.magnitude() > self.MAX_DIST:
    #             break