import glfw
from core.scene import Scene

class Engine:
	#constructor
	def __init__(self):
		#library
		if not glfw.init():
			raise Exception("GLFW initialization failed!")
		#hints
		glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
		glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 6)
		glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
		#window
		self.m_window = glfw.create_window(700, 700, "Window", None, None)
		if not self.m_window:
			glfw.terminate()
			raise Exception("GLFW window initialization failed!")
		#context
		glfw.make_context_current(self.m_window)
		#scene
		self.m_scene = Scene()

	#destructor
	def __del__(self):
		del self.m_scene
		glfw.destroy_window(self.m_window)
		glfw.terminate()

	#run
	def run(self):
		while not glfw.window_should_close(self.m_window):
			glfw.poll_events()
			self.m_scene.draw()
			glfw.swap_buffers(self.m_window)