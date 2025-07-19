from core.scene import Scene
from animations.move import Move
from objects.circle import Circle

class FirstScene(Scene):
	def construct(self):
		c = Circle(radius = 1.0)
		self.add_object(c)
		self.play(Move(c, target = (2, 1), duration = 2.0))