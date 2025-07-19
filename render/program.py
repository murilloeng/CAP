#imports
from render.shader import Shader
from OpenGL.GL import (
	glIsProgram, glDeleteProgram, glCreateProgram, glAttachShader, glLinkProgram, glGetProgramiv, glGetProgramInfoLog, glUseProgram, GL_VERTEX_SHADER, GL_FRAGMENT_SHADER, GL_GEOMETRY_SHADER, GL_LINK_STATUS
)

class Program:
	#constructor
	def __init__(self):
		self.m_id = 0
		self.m_shader_vertex = Shader(GL_VERTEX_SHADER)
		self.m_shader_fragment = Shader(GL_FRAGMENT_SHADER)
		self.m_shader_geometry = Shader(GL_GEOMETRY_SHADER)

	#destructor
	def __del__(self):
		if glIsProgram(self.m_id):
			glDeleteProgram(self.m_id)

	#setup
	def setup(self):
		#shaders
		self.m_shader_vertex.setup()
		self.m_shader_fragment.setup()
		self.m_shader_geometry.setup()
		#create
		self.m_id = glCreateProgram()
		glAttachShader(self.m_id, self.m_shader_vertex.m_id)
		glAttachShader(self.m_id, self.m_shader_fragment.m_id)
		if self.m_shader_geometry.m_id: glAttachShader(self.m_id, self.m_shader_geometry.m_id)
		#link
		glLinkProgram(self.m_id)
		result = glGetProgramiv(self.m_id, GL_LINK_STATUS)
		if not result:
			error = glGetProgramInfoLog(self.m_id).decode()
			raise RuntimeError("Program linking failed:\n%s" % error)

	#bind
	def bind(self):
		glUseProgram(self.m_id)