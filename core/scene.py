#imports
from render.vao import VAO
from render.program import Program

class Scene:
	#constructor
	def __init__(self):
		#data
		self.m_vaos = []
		self.m_objects = []
		self.m_programs = []
		self.m_animations = []
		#model program
		program = Program()
		with open("shaders/model.vert", "r") as file:
			program.m_shader_vertex.m_src = file.read()
		with open("shaders/model.frag", "r") as file:
			program.m_shader_fragment.m_src = file.read()
		program.setup()
		#model vao
		vao = VAO()
		
		#add model
		self.m_vaos.append(vao)
		self.m_programs.append(program)

	#objects
	def add_object(self, object):
		self.m_objects.append(object)

	#animations
	def play(self, animation):
		self.m_animations.append(animation)
		animation.begin()

	#update
	def update(self, dt):
		for animation in self.m_animations:
			animation.update(dt)
		for object in self.m_objects:
			object.update(dt)

	#draw
	def draw(self):
		for object in self.m_objects:
			object.draw()