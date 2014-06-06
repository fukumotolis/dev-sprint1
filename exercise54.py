# This is where Exercise 5.4 goes
# Name: Lisa

def is_triangle(x, y, z):
	if x > (y + z):
		print (x, y, z)							# just for checking purposes
		print 'This cannot be a triangle'
	elif y > (x + z):
		print (x, y, z)
		print 'This cannot be a triangle'
	elif z > (x + y):
		print (x, y, z)
		print 'This cannot be a triangle'
	else:
		print (x, y, z)
		print 'That\'s going to be a nice triangle'

"""
Side sum possibilities are:
x+y	not including z
x+z not including y
y+z not including x
"""
		
is_triangle(5,5,9)
is_triangle(1,2,20)

# could I have done this with nested conditionals?
