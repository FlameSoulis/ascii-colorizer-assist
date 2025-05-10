def unique_symbols(ascii):
	# Remove newlines and spaces
	ascii = ascii.replace("\n", "")
	ascii = ascii.replace(" ", "")
	# Establish our list
	return_list = []
	# It's looping time!
	for c in ascii:
		# If the symbol isn't in the list, add it
		if not c in return_list:
			return_list.append(c)
	# Return our list
	return return_list

def generate_mask(ascii, use_index = False):
	# Grab the unique symbols
	symbols = unique_symbols(ascii)
	for i,c in enumerate(symbols):
		ascii = ascii.replace(c, str((i + 1) * use_index))
	return ascii


if __name__ == "__main__":
	print("Filler")