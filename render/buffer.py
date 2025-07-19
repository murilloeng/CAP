#imports
from OpenGL.GL import glCreateBuffers, glIsBuffer, glDeleteBuffers

class buffer:
	#constructor
	def __init__(self):
		self.m_id = glCreateBuffers(1)

	#destructor
	def __del__(self):
		if glIsBuffer(self.m_id):
			glDeleteBuffers(self.m_id)