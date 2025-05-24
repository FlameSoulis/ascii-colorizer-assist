import os
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

def generate_mask_file(source_file, use_index):
	with open(source_file) as file_handle:
		file_data = file_handle.read()
		new_file_name = list(os.path.splitext(source_file))
		new_file_name[0] += "_mask"
		new_file_name = ''.join(new_file_name)
		with open(new_file_name, 'w') as new_file_handle:
			mask_data = generate_mask(file_data, use_index)
			new_file_handle.write(mask_data)