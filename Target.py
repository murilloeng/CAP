import glfw
import Scene

from OpenGL.GL import *

class Target:
	#constructor
	def __init__(self):
		#setup
		if not glfw.init():
			raise Exception("GLFW can't be initialized")
		#window
		self.m_window = glfw.create_window(700, 700, "Window", None, None)
		if not self.m_window:
			glfw.terminate()
			raise Exception("GLFW window can't be created")
		#scene
		self.m_scene = Scene.Scene()
		#context
		glfw.make_context_current(self.m_window)

	#destructor
	def __del__(self):
		#window
		glfw.destroy_window(self.m_window)
		#library
		glfw.terminate()

	#show
	def show(self):
		while not glfw.window_should_close(self.m_window):
			glfw.poll_events()
			glClear(GL_COLOR_BUFFER_BIT)
			glfw.swap_buffers(self.m_window)