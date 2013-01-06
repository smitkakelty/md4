import hashlib, random, string

print "Enter a hash"
check = rawinput()

table = range(0, 10) + list(string.letters) + list(string.punctuation)

def gen():
	length = random.randint(1, 13)
	attempt = random.sample(table, length)
	attempt = [str(x) for x in attempt]
	return ''.join(attempt)

while 1:
	attempt = gen()
	if hashlib.new("md4", attempt) == check:
		print attempt
		break