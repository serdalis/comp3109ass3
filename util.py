def print_tree(root, out="", level=0):
	if level == 0:
		out += str(root) + "\n"
	else:
		out += '    ' * (level - 1) + "|-( " + str(root) + " )\n"
	for t in root.children:
		out = print_tree(t, out, level + 1)
	return out
	
def is_numeric(value):
	try:
		float(value)
	except ValueError, e:
		return False
	return True
	
def max_locals(tree,max=0,depth=0):
	depth += 1
	if depth > max:
		max = depth
		for child in tree.children:
			tmp = max_locals(child,max,depth+1)
			if tmp > max:
				max = tmp
	return max