
import numpy as np

def circle_draw(r=1, density=100):
    vertices = []
    temp = []
    x1 = np.linspace(r, 0, density, dtype=np.float32)
    y1 = np.sqrt(r**2 - x1**2)
    z = np.zeros(density, dtype=np.float32)
    vertices = vertices + list(zip(x1, y1, z))

    x2 = -1 * np.flip(x1)
    y2 = np.flip(y1)
    vertices = vertices + list(zip(x2, y2, z))

    x3 = -1 * x1
    y3 = -1 * y1
    vertices = vertices + list(zip(x3, y3, z))

    x4 = -1 * x2
    y4 = -1 * y2
    vertices = vertices + list(zip(x4, y4, z))
    return vertices


def _add_vertices(x, y, z, vertices):
    vertices.append([x, y, 0.0])
    vertices.append([x, -y, 0.0])
    vertices.append([-x, y, 0.0])
    vertices.append([-x, -y, 0.0])
    vertices.append([y, x, 0.0])
    vertices.append([-y, x, 0.0])
    vertices.append([y, -x, 0.0])
    vertices.append([-y, -x, 0.0])


def mid_point_circle(r: float=1.0, step: float=1.0):
    div = 0.0
    scaled = False      #Vartices are Scaled or not
    #Scale the circle if too small
    if r < 100:
        div = 100 / r
        r = r * div
        scaled = True

    x, y = 0.0, r

    xEnd = r/np.sqrt(2)
    decision = 1.0 - r
    vertices = []

    while x < xEnd:
        _add_vertices(x, y, 0.0, vertices)
        if decision > 0:
            x, y = x+step, y-step
            delSE = 2*x - 2*y + 5
            decision = decision + delSE
        else:
            x, y = x+step, y
            delE = 2*x + 3
            decision = decision + delE

    #return the array back to previous state(before scaling
    if scaled:
        vertices = np.array(vertices, dtype=np.float32) / div
    else:
        vertices = np.array(vertices, dtype=np.float32)
    return vertices


if __name__ == '__main__':
    mid_point_circle(step=0.1)



