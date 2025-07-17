from OpenGL.GL import *

class Shader:
	#constructor
	def __init__(self, type):
		self.m_src = ""
		self.m_type = type
		self.m_id = glCreateShader(type)
	
	#destructor
	def __del__(self):
		if glIsShader(self.m_id):
			glDeleteShader(self.m_id)
	
	#setup
	def setup(self):
		glCompileShader(self.m_id)
		if glGetShaderiv(self.m_id, GL_COMPILE_STATUS) != GL_TRUE:
			raise RuntimeError(glGetShaderInfoLog(self.m_id).decode())