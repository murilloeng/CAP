import glfw
from core.scene import Scene

class Engine:
	#constructor
	def __init__(self, scene : Scene):
		#library
		if not glfw.init():
			raise Exception("GLFW initialization failed!")
		#window
		self.m_window = glfw.create_window(700, 700, "Window", None, None)
		if not self.m_window:
			glfw.terminate()
			raise Exception("GLFW window initialization failed!")
		#context
		glfw.make_context_current(self.m_window)
		#scene
		self.m_scene = scene

	#destructor
	def __del__(self):
		glfw.destroy_window(self.m_window)
		glfw.terminate()

	#run
	def run(self):
		while not glfw.window_should_close(self.m_window):
			glfw.poll_events()
			glfw.swap_buffers(self.m_window)