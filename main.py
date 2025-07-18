#imports
from core.scene import Scene
from core.engine import Engine

#main
if __name__ == "__main__":
	#data
	scene = Scene()
	engine = Engine(scene)
	#run
	engine.run()