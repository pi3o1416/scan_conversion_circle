
import glfw
import numpy as np
from OpenGL.GL import *


class Window:
    def __init__(self, win_x: int, win_y: int, pos_x: int, pos_y: int):
        """
        Initialize glfw window and with window size and position
        and make it current context
        Parameter:
        win_x   : window size in x axis (int)
        win_y   : window size in y axis (int)
        pos_x   : window position in x axis (int)
        pos_y   : window position in y axis (int)

        Return: None
        """
        self.vertices = None
        self.colors = None

        if not glfw.init():
            raise Exception("glfw can not be initialize")

        self.window = glfw.create_window(
            win_x, win_y, "My OpenGL window", None, None)
        if not self.window:
            glfw.terminate()
            raise Exception("glfw window can not be created")

        glfw.set_window_pos(self.window, pos_x, pos_y)
        glfw.make_context_current(self.window)
        glPointSize(2)

    def __del__(self):
        glfw.terminate()

    def set_color(self, red: float, green: float, blue: float, alpha: float = 1):
        """
        Set Color for window in rgb
        Parameters :
        red     :(float)
        green   :(float)
        blue    :(float)
        alpha   :(float)

        Return : None
        """
        glClearColor(red, green, blue, alpha)

    def set_vertices(self, vertices):
        """
        Set Vertices to display in array
        Parameters:
        vertices    : new vertices (np.array)

        return : None
        """
        self.vertices = vertices
        max_val = np.max(self.vertices)
        if max_val > 1.0:
            self.vertices = self.vertices / (max_val + 0.001)  #Array Scaling

        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, self.vertices)

    def main_loop(self, mode):
        while not glfw.window_should_close(self.window):
            glfw.poll_events()
            glClear(GL_COLOR_BUFFER_BIT)
            glDrawArrays(mode, 0, len(self.vertices))

            glfw.swap_buffers(self.window)
