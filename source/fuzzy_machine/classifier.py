from source.fuzzy_machine.fuzzy_rules import is_versicolor, is_setosa, is_virginica, is_medium_sepal_versicolor
def classify(sepal_l, sepal_w, petal_l, petal_w):
	rules_membership = []
	rules_membership.append(is_versicolor(sepal_l, sepal_w, petal_l, petal_w))
	rules_membership.append(is_setosa(petal_l, petal_w))
	rules_membership.append(is_virginica(sepal_w, petal_l, petal_w))
	rules_membership.append(is_medium_sepal_versicolor(sepal_l, sepal_w, petal_l, petal_w))


	# find the iris with max membership
	max_membership = 0
	iris = 0
	for rm in rules_membership:
		if rm["membership"] > max_membership:
			max_membership = rm["membership"]
			iris = rm["iris"]

	return iris
