from OpenGL.GL import *

class Scene:
	def __init__(self):
		self.m_vaos = []
		self.m_vbos = []
		self.m_ibos = []
		self.m_programs = []
		self.m_textures = []

	@staticmethod
	def background(color):
		glClearColor(color[0], color[1], color[2], color[3])