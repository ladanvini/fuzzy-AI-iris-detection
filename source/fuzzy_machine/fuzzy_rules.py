from source.fuzzy_machine.membership_funcs import intersect, union, short, long, medium
from source.models import Iris

def is_versicolor(sepal_length, sepal_width, petal_length, petal_width):
	membership = intersect(
                        intersect(
                            union(short(sepal_length),long(sepal_length)),
                            union(medium(sepal_width), long(sepal_width))
                            ),
                        intersect(
                            union(medium(petal_length), long(petal_length)),
                            medium(petal_width)
                            )
                        )
	return {"iris":Iris.VERSICOLOR.value, "membership":membership}

def is_setosa(petal_length, petal_width):
	membership = intersect( union(short(petal_length),medium(petal_length)), short(petal_width))
	return {"iris":Iris.SETOSA.value, "membership":membership}

def is_virginica(sepal_width, petal_length, petal_width):
	membership = intersect(
        intersect(
            union(short(sepal_width), medium(sepal_width)),
            long(petal_length)
            ),
        long(petal_width)
        )
	return {"iris":Iris.VIRGINICA.value, "membership":membership}

def is_medium_sepal_versicolor(sepal_length, sepal_width, petal_length, petal_width):
	membership = intersect(
        intersect(
            medium(sepal_length),
            union(short(sepal_width),medium(sepal_width))
            ),
        intersect(short(petal_length),long(petal_width))
        )
	return {"iris":Iris.VERSICOLOR.value, "membership":membership}


