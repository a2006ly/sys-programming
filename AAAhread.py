import threading
import subprocess


class test(threading.Thread):
	def __init__(self):
		  threading.Thread.__init__(self)

	def run(self):
		print("test")
		p = subprocess.Popen("[dir]",stdin=susprocess.PIPE,stdout=subprocess.PIPE,shell=TRUE)
		a,b = p.ccommunicate()
		
		

if __name__ == "__main__":

	t = test()
	t.start()