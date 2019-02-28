
def output(slides, file):
	f = open(file, "w")

	f.write('{}\n'.format(len(slides)))

	for i in slides:
		try:
			f.write('{} {}\n'.format(i[0], i[1]))
		except:
			#Int
			f.write('{}\n'.format(i))
			