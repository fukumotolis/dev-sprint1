# Koch curve (5.6)

# Name: Lisa 

from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()
jennifer = Turtle()	

def koch(t, l):
	if l < 3:		# if l is less than 3, straight line	
		fd(t, l)
		return
	else:
		d = l / 3
		koch(t, d)	
		lt(t, 60)
		koch(t, d)
		rt(t, 120)
		koch(t, d)
		lt(t, 60)
		koch(t, d)

# koch(bob, 2)		
koch(bob, 100)		

# is else unnecessary?

def snowflake(t, l):	# draws 3 Koch curves of length l
	for i in range(3):
		koch(t,l)

snowflake(jennifer, 60)

wait_for_user()