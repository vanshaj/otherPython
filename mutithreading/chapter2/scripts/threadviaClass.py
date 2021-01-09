#!/bin/python
from threading import Thread
class mythreadClass(Thread): # inherit Thread class from threading module
	def __init__(self):
		print("Hello:")
		Thread.__init__(self) #will call the parent class constructor
	
	def run(self): # this code will get executed when start method is called
		print("Thread running")
	
if __name__ == '__main__':
	myclass = mythreadClass()
	print("Created thread object")
	myclass.start() # here the run method will be called thread enters running state
	myclass.join() #here the thread will be stopped

		
