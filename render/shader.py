#imports
from OpenGL.GL import (
	c_int, glIsShader, glDeleteShader, glCreateShader, glShaderSource, glCompileShader, glGetShaderiv, glGetShaderInfoLog, GL_VERTEX_SHADER, GL_FRAGMENT_SHADER, GL_COMPILE_STATUS
)

class Shader:
	#constructor
	def __init__(self, type : c_int):
		self.m_id = 0
		self.m_src = ""
		self.m_type = type

	#destructor
	def __del__(self):
		if glIsShader(self.m_id):
			glDeleteShader(self.m_id)
	
	#setup
	def setup(self):
		if self.m_src:
			#create
			self.m_id = glCreateShader(self.m_type)
			#source
			glShaderSource(self.m_id, self.m_src)
			#compile
			glCompileShader(self.m_id)
			# Check compilation status
			result = glGetShaderiv(self.m_id, GL_COMPILE_STATUS)
			if not result:
				error = glGetShaderInfoLog(self.m_id).decode()
				raise RuntimeError("Shader compilation failed:\n%s" % error)
		else:
			if self.m_type == GL_VERTEX_SHADER:
				raise Exception("Vertex shader with no source!")
			if self.m_type == GL_FRAGMENT_SHADER:
				raise Exception("Fragment shader with no source!")