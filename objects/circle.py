from core.object import Object

class Circle(Object):
	def __init__(self, radius = 1.0):
		super().__init__()
		self.radius = radius

	def draw(self):
		print(f"Drawing Circle at {self.position} with radius {self.radius}")