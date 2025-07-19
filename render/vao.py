#imports
from OpenGL.GL import glGenVertexArrays, glIsVertexArray, glDeleteVertexArrays, glBindVertexArray

class VAO:
	#constructor
	def __init__(self):
		self.m_id = glGenVertexArrays(1)

	#destructor
	def __del__(self):
		if glIsVertexArray(self.m_id):
			glDeleteVertexArrays(self.m_id)
	
	#bind
	def bind(self):
		glBindVertexArray(self.m_id)