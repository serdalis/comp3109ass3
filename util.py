def print_tree(root, out="", level=0):
	if level == 0:
		out += str(root) + "\n"
	else:
		out += '    ' * (level - 1) + "|-( " + str(root) + " )\n"
	for t in root.children:
		out = print_tree(t, out, level + 1)
	return out
