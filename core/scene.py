class Scene:
	def __init__(self):
		self.objects = []
		self.animations = []

	def add(self, obj):
		self.objects.append(obj)

	def play(self, animation):
		self.animations.append(animation)
		animation.begin()

	def update(self, dt):
		for animation in self.animations:
			animation.update(dt)
		for object in self.objects:
			object.update(dt)

	def draw(self):
		for object in self.objects:
			object.draw()