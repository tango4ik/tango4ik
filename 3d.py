#half working 3d renderer
#pretty unoptimized
#im not that good
import pygame as pg
import numpy as np
def load_vertices_from_obj(file_path):
    vertices = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('v '):  # Vertex lines start with 'v '
                # Split the line and convert the coordinates to floats
                vertex = [float(coord) for coord in line.split()[1:]] 
                vertices.append(vertex)
    return vertices


pg.init()
#put model location
#vertices = load_vertices_from_obj('monkey.obj')
screen = pg.display.set_mode((800, 600),pg.RESIZABLE)
done = False
focal = 300
cam = [0.001,0.001,5]
def rotate_x(x, y, z, angle):
    new_y = y * np.cos(angle) - z * np.sin(angle)
    new_z = y * np.sin(angle) + z * np.cos(angle)
    return x, new_y, new_z

def rotate_y(x, y, z, angle):
    new_x = x * np.cos(angle) + z * np.sin(angle)
    new_z = -x * np.sin(angle) + z * np.cos(angle)
    return new_x, y, new_z

def rotate_z(x, y, z, angle):
    new_x = x * np.cos(angle) - y * np.sin(angle)
    new_y = x * np.sin(angle) + y * np.cos(angle)
    return new_x, new_y, z

def project(x, y, z,ax,ay,az):

    x += cam[0]
    y += cam[1]
    z += cam[2]
    x,y,z = rotate_x(x,y,z,ax)
    x,y,z = rotate_y(x,y,z,ay)
    x,y,z = rotate_z(x,y,z,az)
    pos = [focal * (x/z) +400, focal *(y/z)+300]
    
    pg.draw.circle(screen, (255, 255, 255), pos, 5)
def re(x,y,z,ax,ay,az):
    x += cam[0]
    y += cam[1]
    z += cam[2]
    x,y,z = rotate_x(x,y,z,ax)
    x,y,z = rotate_y(x,y,z,ay)
    x,y,z = rotate_z(x,y,z,az)
    pos = [focal * (x/z) +400, focal *(y/z)+300]
    return pos
def draw_line(pos1, pos2):
    pg.draw.line(screen, (255, 255, 255), pos1, pos2)
def cube(x,y,z,ax,ay,az):
    ax = np.radians(ax)
    ay = np.radians(ay)
    az = np.radians(az)
    project(x+0,y+0,z+0,ax,ay,az)
    project(x+2,y+0,z+0,ax,ay,az)
    project(x+0,y+2,z+0,ax,ay,az)
    project(x+2,y+2,z+0,ax,ay,az)
    project(x+0,y+0,z+2,ax,ay,az)
    project(x+2,y+0,z+2,ax,ay,az)
    project(x+0,y+2,z+2,ax,ay,az)
    project(x+2,y+2,z+2,ax,ay,az)
def model(x,y,z,ax,ay,az,m):
    for i in range(len(m)):
        project(m[i][0]+x,m[i][1]+y,m[i][2]+z,ax,ay,az)
        if i < len(m)-1:
           pg.draw.line(screen, (255, 255, 255), re(m[i][0]+x,m[i][1]+y,m[i][2]+z,ax,ay,az), re(m[i+1][0]+x,m[i+1][1]+y,m[i+1][2]+z,ax,ay,az))
rx = 0
ry = 0
rz = 0
clock = pg.time.Clock()
#m = load_vertices_from_obj('text.obj')
def draw():
    screen.fill((0, 0, 0))
    cube(10,5,0,-rx,-ry,0)
    #model(10,5,0,-rx / 1,-ry / 1,rz,m)
    pg.display.flip()
speed = 10
rs = 1
while not done:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    keys = pg.key.get_pressed()
    if keys[pg.K_s]:
        cam[2] += np.sin(np.radians(rz)) * 0.01 * speed * 10
    if keys[pg.K_w]:
        cam[2] += -np.sin(np.radians(rz)) * 0.01 * speed * 10
    if keys[pg.K_d]:
        cam[0] += np.cos(np.radians(rx)) * 0.01 * speed * 10
    if keys[pg.K_a]:
        cam[0] += -np.cos(np.radians(rx)) * 0.01 * speed * 10
    if keys[pg.K_e]:
        cam[1] += np.cos(np.radians(ry)) * 0.01 * speed
    if keys[pg.K_q]:
        cam[1] += -np.cos(np.radians(ry)) * 0.01 * speed
    if keys[pg.K_UP]:
        rx += 0.1 *rs
    if keys[pg.K_DOWN]:
        rx -= 0.1 * rs
    if keys[pg.K_RIGHT]:
        ry += 0.1 *rs
    if keys[pg.K_LEFT]:
        ry -= 0.1 * rs
    if keys[pg.K_PAGEDOWN]:
        rz += 0.1 * rs
    if keys[pg.K_PAGEUP]:
        rz -= 0.1 * rs
    fps = clock.tick(60)
    pg.display.set_caption(f"fps: {fps}")
    draw()
