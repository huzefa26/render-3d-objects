import pygame as pg
from matrix_functions import *
from numba import njit


@njit(fastmath=True)
def np_any(arr, x):
    return np.any(arr == x)

class Object3D:

    def __init__(self, render, vertices, faces):
        self.render = render
        self.vertices = np.array(vertices)
        self.faces = np.array(faces)

        self.font = pg.font.SysFont('Arial', 30, bold=True)
        self.colored_faces = [(face, pg.Color('orange')) for face in self.faces]
        self.movement_flag, self.draw_vertices = False, False
        self.label = ''
    
    def draw(self):
        self.screen_projection()
        self.movement()
    
    def movement(self):
        if self.movement_flag:
            self.rotate_y(pg.time.get_ticks() % 0.005)
    
    def screen_projection(self):
        vertices = self.vertices @ self.render.camera.camera_matrix()
        vertices = vertices @ self.render.projection.projection_matrix

        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices[(vertices > 2)|(vertices < -2)] = 0

        vertices = vertices @ self.render.projection.to_screen_matrix
        vertices = vertices[:, :2]

        for face_index, colored_face in enumerate(self.colored_faces):
            face, color = colored_face
            polygon = vertices[face]
            if not np_any(polygon, self.render.H_WIDTH) or not np_any(polygon, self.render.H_HEIGHT):
                pg.draw.polygon(self.render.screen, color, polygon, 1)
                if self.label:
                    text = self.font.render(self.label[face_index], True, pg.Color('white'))
                    self.render.screen.blit(text, polygon[-1])
        if self.draw_vertices:
            for vertex in vertices:
                if not np_any(polygon, self.render.H_WIDTH) or not np_any(polygon, self.render.H_HEIGHT):
                    pg.draw.circle(self.render.screen, pg.Color('white'), vertex, 2)

    def translate(self, pos):
        self.vertices = self.vertices @ translate(pos)

    def scale(self, aspect):
        self.vertices = self.vertices @ scale(aspect)

    def rotate_x(self, angle):
        self.vertices = self.vertices @ rotate_x(angle)

    def rotate_y(self, angle):
        self.vertices = self.vertices @ rotate_y(angle)

    def rotate_z(self, angle):
        self.vertices = self.vertices @ rotate_z(angle)

class Axes(Object3D):
    def __init__(self, render):
        super().__init__(render)
        self.vertices = np.array([(0,0,0,1), (1,0,0,1), (0,1,0,1), (0,0,1,1)])
        self.faces = np.array([(0,1), (0,2), (0,3)])
        self.colors = [pg.Color('red'), pg.Color('green'), pg.Color('blue')]
        self.colored_faces = [(face, color) for face, color in zip(self.faces, self.colors)]
        self.draw_vertices = False
        self.label = 'XYZ'



'''
Cube 


        self.vertices = np.array([
            (0, 0, 0, 1),
            (0, 1, 0, 1),
            (1, 1, 0, 1),
            (1, 0, 0, 1),
            (0, 0, 1, 1),
            (0, 1, 1, 1),
            (1, 1, 1, 1),
            (1, 0, 1, 1),
        ])

        self.faces = np.array([
            (0, 1, 2, 3),
            (4, 5, 6, 7),
            (0, 4, 5, 1),
            (2, 3, 7, 6),
            (1, 2, 6, 5),
            (0, 3, 7, 4),
        ])

'''