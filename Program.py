from OpenGL.GL import *
from Shader import Shader

class Program:
	#constructor
	def __init__(self):
		self.m_id = glCreateProgram()
		self.m_shader_vertex = Shader()
		self.m_shader_fragment = Shader()
		self.m_shader_geometry = Shader()
	
	#destructor
	def __del__(self):
		if glIsProgram(self.m_id):
			glDeleteProgram(self.m_id)
	
	#setup
	def setup(self):
		#setup
		self.m_shader_vertex.setup()
		self.m_shader_fragment.setup()
		if self.m_shader_geometry.m_src: self.m_shader_geometry.setup()
		#attach
		glAttachShader(self.m_id, self.m_shader_vertex.m_id)
		glAttachShader(self.m_id, self.m_shader_fragment.m_id)
		if self.m_shader_geometry.m_src: glAttachShader(self.m_id, self.m_shader_geometry.m_id)
		#link
		glLinkProgram(self.m_id)
		if glGetProgramiv(self.m_id, GL_LINK_STATUS) != GL_TRUE:
			raise RuntimeError(glGetProgramInfoLog(self.m_id).decode())
