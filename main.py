from object_3d import Object3D, Axes
from camera import Camera
from projection import Projection
import pygame as pg

# https://www.youtube.com/watch?v=M_Hx0g5vFko

class SoftwareRender:
    def __init__(self, filepath=None, camera_moving_speed=None, camera_rotation_speed=None):
        pg.init()
        self.RESOLUTION = self.WIDTH, self.HEIGHT = 1600, 900
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RESOLUTION)
        self.clock = pg.time.Clock()
        self.create_objects(filepath, camera_moving_speed, camera_rotation_speed)
    
    # def create_object_cube(self):
    #     self.camera = Camera(self, [0.5, 1, -4])
    #     self.projection = Projection(self)
    #     self.object = Object3D(self)
    #     self.object.translate([0.2, 0.4, 0.2])
        
    #     self.axes = Axes(self)
    #     self.axes.translate([0.7, 0.9, 0.7])
    #     self.world_axes = Axes(self)
    #     self.world_axes.movement_flag = False
    #     self.world_axes.scale(2.5)
    #     self.world_axes.translate([1e-4, 1e-4, 1e-4])
    
    # def draw_cube(self):
    #     self.screen.fill(pg.Color('darkslategray'))
    #     self.world_axes.draw()
    #     self.axes.draw()
    #     self.object.draw()

    def create_objects(self, filepath, camera_moving_speed, camera_rotation_speed):
        self.camera = Camera(self, [-5, 5, -50], moving_speed=camera_moving_speed, rotation_speed=camera_rotation_speed)
        self.projection = Projection(self)
        self.object = self.get_objects_from_file(filepath)

    def get_objects_from_file(self, filepath):
        vertices, faces = [], []
        with open(filepath) as fh:
            for line in fh.readlines():
                if line.startswith('v '):
                    vertices.append(list(map(float, line.split()[1:])) + [1])
                elif line.startswith('f'):
                    faces.append([
                        int(face.split('/')[0]) - 1
                        for face in line.split()[1:]
                    ])
        return Object3D(self, vertices, faces)

    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))
        self.object.draw()

    
    def run(self):
        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    app = SoftwareRender(
        filepath='objects/tank.obj',
        camera_moving_speed=0.5, camera_rotation_speed=0.02
        )
    app.run()