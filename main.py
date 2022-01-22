
from window import Window
from OpenGL import GL
from scan_conversion_circle import mid_point_circle, circle_draw 

def main():

#    vertices = circle_draw(r=1, density=10)
    vertices = mid_point_circle(r=200)

    window = Window(720, 720, 400, 200)
    window.set_color(0, 0.1, 0.1, 1)
    window.set_vertices(vertices)
    window.main_loop(GL.GL_POINTS)

if __name__ == "__main__":
    main()

