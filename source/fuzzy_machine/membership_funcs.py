def short(x):
	if x < 0.6:
		return 1 - (1/0.6)*x
	return 0

def medium(x):
    if x < 0.6:
        return (1/0.6)*x
    return -(1/0.4)*(x-1)

def long(x):
    if x < 0.6:
        return 0
    return (1/0.4)*(x-0.6)

def union(x1, x2):
	return max(x1,x2)

def intersect(x1,x2):
	return min(x1, x2)

