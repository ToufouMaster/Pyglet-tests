import pyglet
from player import *

MAP = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
G_MAP = []

MAP_IMAGES = {
    'GROUND': pyglet.image.load('./src/0.png'),
    'WALL': pyglet.image.load('./src/1.png'),
    'ERROR': pyglet.image.load('./src/no_texture.png')
}

window = pyglet.window.Window()
# Creating graphics groups
batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
mapground = pyglet.graphics.OrderedGroup(1)
playerground = pyglet.graphics.OrderedGroup(2)
rayground = pyglet.graphics.OrderedGroup(3)
foreground = pyglet.graphics.OrderedGroup(4)

def update_map(px, py, csx, csy, scale, map):
    new_gmap = map
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                new_gmap[y][x] = pyglet.sprite.Sprite(MAP_IMAGES['GROUND'], x=px+(x*csx)*scale, y=py-(y*csy)*scale, batch=batch, group=mapground)
            elif map[y][x] == 1:
                new_gmap[y][x] = pyglet.sprite.Sprite(MAP_IMAGES['WALL'], x=px+(x*csx)*scale, y=py-(y*csy)*scale, batch=batch, group=mapground)
            else:
                new_gmap[y][x] = pyglet.sprite.Sprite(MAP_IMAGES['ERROR'], x=px+(x*csx)*scale, y=py-(y*csy)*scale, batch=batch, group=mapground)
            new_gmap[y][x].scale = scale
    return new_gmap

def draw_map(g_map):
    for y in g_map:
        for x in y:
            x.draw()

@window.event
def on_draw():
    window.clear()
    draw_map(G_MAP)
    player.draw(batch, playerground)
    player.draw_ray_cast_lines(100, batch, rayground)

map_scale = 2
G_MAP = update_map(0, window.height-16*map_scale, 16, 16, map_scale, MAP)
player_size_x = 32
player_size_y = 32
player = Player((3*16)*map_scale-(player_size_x/2), (3*16)*map_scale-(player_size_y/2), player_size_x, player_size_y, 3, -90)
player.setup_ray_cast_lines(30)
pyglet.app.run()