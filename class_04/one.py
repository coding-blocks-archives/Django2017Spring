class A:
	def __init__(self, x=1, y=2):
		self.x = x
		self.y = y

def separate():
	print '======================================='


a = [1]*10
a[2] = 5
a[5] = 10
b = [A() for ix in range(5)]

print a

for ix in b:
	print ix

b[2].x = 9


for ix in b:
	print ix.x

separate()

for ix in range(1, 6):
	print '@'*ix

separate()

a = [A(1, 3), A(5, -9), A(0, 52), A(-4, 12)]
b = sorted(a, key=lambda z:z.y)

for ix in a:
	print ix.x, ix.y

separate()

for ix in b:
	print ix.x, ix.y

separate()
separate()

def incVal(val, lst=None):
	if lst is None:
		lst = list()
	lst.append(val)
	return lst

v1 = incVal(10)
v2 = incVal('ab', [])
v3 = incVal(45)

print v1	# [10]
print v2	# ['ab']
print v3	# [10, 45], [45]

separate()
separate()

f = lambda x: x*2

print f(1)
