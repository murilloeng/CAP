from abc import ABC, abstractmethod

class Object(ABC):
	def __init__(self):
		self.opacity = 1.0
		self.position = [0.0, 0.0, 0.0]

	@abstractmethod
	def draw(self):
		pass

	def update(self, dt):
		pass