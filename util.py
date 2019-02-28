
def points(tags1, tags2):
	a = [tag for tag in tags1 if tag in tags2]
	b = [tag for tag in tags1 if tag not in a]
	c = [tag for tag in tags2 if tag not in a]
	
	return min([a,b,c])
