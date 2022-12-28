from app import App
import pygame

from scene_manager.scene import Scene
from scene_manager.scene_objects import *

from renderer import RayMarchingRenderer

import colors


def draw_circle(circle: Circle, surface: pygame.Surface):
    pygame.draw.circle(surface, circle.color, circle.center.xy, circle.radius, 2)


def min_sdf(p: pygame.Vector2, scene: Scene):
    m = scene.scene_objects[0].sdf(p)
    for scene_object in scene.scene_objects:
        if scene_object.sdf(p) < m:
            m = scene_object.sdf(p)
    return m


class Main(App):
    
    def __init__(self, width: int = 600, height: int = 600, fps: float = 120):
        super().__init__(width, height, fps)
        self.drawn = False
        self.scene = Scene(
            # Circle((50, 50, 50), 10, colors.BLUE),
            Circle((-20, 0, 35), 30, colors.BLUE),
            Circle((20, 0, 35), 30, colors.RED)
            # Circle((100, 100, 100), 50, colors.RED)
        )
        self.renderer = RayMarchingRenderer(self.surface)
    
    def update(self, dt):
        super().update(dt)
    
    def draw(self):
        super().draw()
        # self.surface.fill((0, 0, 0))
        mouse = pygame.Vector2(pygame.mouse.get_pos())
        # for scene_object in self.scene.scene_objects:
        #     draw_circle(scene_object, self.surface)
        #     pygame.draw.circle(self.surface, (255, 255, 255), mouse, min_sdf(mouse, self.scene), 1)
        if not self.drawn:
            self.renderer.render(
                # (mouse - self.renderer.camera).normalize(),
                self.scene
            )
        self.drawn = True
        # pygame.draw.circle(self.surface, WHITE, self.renderer.camera, 2)
        # pygame.draw.line(self.surface, WHITE, self.renderer.camera, mouse)
        
        # for object in self.scene.scene_objects:
        #     draw_circle(object, self.surface)

    def event_handler(self, event: pygame.event.Event):
        super().event_handler(event)


if __name__ == '__main__':
    Main().run()