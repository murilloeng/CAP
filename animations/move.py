class Move:
	def __init__(self, obj, target, duration = 1.0):
		self.obj = obj
		self.start = obj.position.copy()
		self.target = list(target)
		self.duration = duration
		self.elapsed = 0.0

	def begin(self):
		self.elapsed = 0.0

	def update(self, dt):
		self.elapsed += dt
		t = min(self.elapsed / self.duration, 1.0)
		self.obj.position[0] = self.start[0] + (self.target[0] - self.start[0]) * t
		self.obj.position[1] = self.start[1] + (self.target[1] - self.start[1]) * t