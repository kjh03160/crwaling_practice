import time

def time_of_function(function):
	before = time.clock()
	fucntion()
	after = time.clock()
	return after - before