import pyglet

MAP = [
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,1,1,1,0],
    [0,0,1,0,0],
    [0,0,0,0,2],
]

MAP_IMAGES = {
    'GROUND': pyglet.image.load('./src/0.png'),
    'WALL': pyglet.image.load('./src/1.png'),
    'ERROR': pyglet.image.load('./src/no_texture.png')
}

G_MAP = []

window = pyglet.window.Window()
# Creating graphics groups
batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
mapground = pyglet.graphics.OrderedGroup(1)
foreground = pyglet.graphics.OrderedGroup(2)

def update_map(px, py, csx, csy, map):
    new_gmap = map
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                new_gmap[y][x] = pyglet.sprite.Sprite(MAP_IMAGES['GROUND'], x=px+(x*csx), y=py-(y*csy), batch=batch, group=mapground)
            elif map[y][x] == 1:
                new_gmap[y][x] = pyglet.sprite.Sprite(MAP_IMAGES['WALL'], x=px+(x*csx), y=py-(y*csy), batch=batch, group=mapground)
            else:
                new_gmap[y][x] = pyglet.sprite.Sprite(MAP_IMAGES['ERROR'], x=px+(x*csx), y=py-(y*csy), batch=batch, group=mapground)
    return new_gmap

G_MAP = update_map(0, window.height-16, 16, 16, MAP)

def draw_map(g_map):
    for y in g_map:
        for x in y:
            x.draw()

@window.event
def on_draw():
    window.clear()
    draw_map(G_MAP)

pyglet.app.run()