import math

def addMe(a, b):
	return a+b


def root(p):
	return math.sqrt(p)


class MyClass:
	def __init__(self, cname='', n_students=0, location=''):
		self.cname = cname
		self.n_students = n_students
		self.location = location

	def getLocation(self):
		return self.location

	def className(self):
		return self.cname


class Dummy:
	pass


if __name__ == '__main__':
	print "This is a package"
	try:
		print "aaaaaa"
		print 'a' + 1
		print '111111111'
	except:
		print "saved"
