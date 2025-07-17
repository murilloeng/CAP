# import glfw
# import numpy as np

# from OpenGL.GL import *

# def compile_shader(src, shader_type):
# 	shader = glCreateShader(shader_type)
# 	glShaderSource(shader, src)
# 	glCompileShader(shader)
# 	if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
# 		raise RuntimeError(glGetShaderInfoLog(shader).decode())
# 	return shader

# def create_shader_program(vertex_src, fragment_src):
# 	vertex_shader = compile_shader(vertex_src, GL_VERTEX_SHADER)
# 	fragment_shader = compile_shader(fragment_src, GL_FRAGMENT_SHADER)
# 	program = glCreateProgram()
# 	glAttachShader(program, vertex_shader)
# 	glAttachShader(program, fragment_shader)
# 	glLinkProgram(program)
# 	if glGetProgramiv(program, GL_LINK_STATUS) != GL_TRUE:
# 		raise RuntimeError(glGetProgramInfoLog(program).decode())
# 	glDeleteShader(vertex_shader)
# 	glDeleteShader(fragment_shader)
# 	return program

# # Initialize GLFW
# if not glfw.init():
# 	raise Exception("GLFW can't be initialized")

# # Create window
# window = glfw.create_window(800, 600, "OpenGL with Shaders", None, None)
# if not window:
# 	glfw.terminate()
# 	raise Exception("GLFW window can't be created")

# glfw.make_context_current(window)

# # Triangle vertices
# triangle = np.array([
# 	[-0.5, -0.5, 0.0],
# 	[ 0.5, -0.5, 0.0],
# 	[ 0.0,  0.5, 0.0],
# ], dtype=np.float32)

# # Vertex Array Object and Vertex Buffer Object
# VAO = glGenVertexArrays(1)
# VBO = glGenBuffers(1)

# glBindVertexArray(VAO)

# glBindBuffer(GL_ARRAY_BUFFER, VBO)
# glBufferData(GL_ARRAY_BUFFER, triangle.nbytes, triangle, GL_STATIC_DRAW)

# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
# glEnableVertexAttribArray(0)

# # Create and use shader program
# src_vert = open("shd/main.vert", "r").read()
# src_frag = open("shd/main.frag", "r").read()
# shader = create_shader_program(src_vert, src_frag)
# glUseProgram(shader)

# # Main loop
# while not glfw.window_should_close(window):
# 	glfw.poll_events()
# 	glClear(GL_COLOR_BUFFER_BIT)
# 	glBindVertexArray(VAO)
# 	glDrawArrays(GL_TRIANGLES, 0, 3)
# 	glfw.swap_buffers(window)

# # Cleanup
# glDeleteVertexArrays(1, [VAO])
# glDeleteBuffers(1, [VBO])
# glDeleteProgram(shader)
# glfw.terminate()

import Target

Target.Target().show()