a = range(20, 10, -2) + [-70]
# print sum(a)

if sum(a)<10:
	print "One"
elif (sum(a) >= 10 and sum(a) < 15):
	print "None"
else:
	print "Yes"


d = {}

d[0] = 'shubham'
d['a'] = 'b'
d[1] = 12

print type(None)

a = """This
is 
a
multi-line
comment. But is it a string??
"""

b = a.split()
print len(b)

for i in range(len(b)):
	print i, b[i]


i = 0
while True:
	if (i%2 == 0):
		print i,
	elif i%3==0:
		i += 1
		continue
	elif i==5:
		pass
	elif i==7:
		break
	print '-------------'
	i+=1

print '----------------------------------'

def fname(*args, **kwargs):
	print args
	print kwargs
	return sum(args)/float(len(args))
	#return a + b


print fname(3, 3, 3, 2, 1, 200, 1, -10, v1=10, v2=120)
a = fname
print a(10, 12)