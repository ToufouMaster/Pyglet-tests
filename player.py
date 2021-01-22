import pyglet
import math

class Player:

    def __init__(self, x, y, sx, sy, speed, view_angle, fov = 80):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.speed = speed
        self.view_angle = view_angle
        self.fov = fov
        self.ray_lines = []
    
    def draw(self, batch, layer):
        rect = pyglet.shapes.Rectangle(self.x, self.y, self.sx, self.sy, color=(250,50,50), batch=batch, group=layer)
        rect.draw()
    
    def setup_ray_cast_lines(self, nmb):
        angle = 360/nmb
        for i in range(nmb):
            self.ray_lines.append(math.radians(i*angle))

    def draw_ray_cast_lines(self, view_distance, batch, layer):
        for i in range(len(self.ray_lines)):
            line = pyglet.shapes.Line(self.x+self.sx/2, self.y+self.sy/2, (self.x+self.sx/2)+(math.cos(self.ray_lines[i])*view_distance), (self.y+self.sy/2)+(math.sin(self.ray_lines[i])*view_distance), width=1, color=(50, 255, 50), batch=batch, group=layer)
            line.draw()

    # TODO:
    # def detect_end_of_line(map?):
        # with the map detext at every tile if the tile is a wall
        # draw a point at the end of line position
        # return the end of line point i think

    # Think about the 3D Renderer!