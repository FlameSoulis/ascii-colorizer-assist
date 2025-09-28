import os

def check_file(file_name):
	if not os.path.exists(file_name):
		raise Exception("does not exist")
	if not os.path.isfile(file_name):
		raise Exception("is not a file")

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


def merge_mask(source_file, mask_file):
	# make sure the files are the same size
	if os.path.getsize(source_file) != os.path.getsize(mask_file):
		raise Exception("Source file does not match size of mask file!")
	with open(source_file) as source_handle:
		with open(mask_file) as mask_handle:
			new_ascii = ""
			source_ascii = source_handle.read()
			mask_data = mask_handle.read()
			color_code = -1
			# Break it down, line by line
			source_lines = source_ascii.split("\n")
			mask_lines = mask_data.split("\n")
			for index, current_line in enumerate(source_lines):
				for letter_index in range(len(current_line)):
					#Check if our color code has changed and isn't space
					if mask_lines[index][letter_index] != color_code:
						if mask_lines[index][letter_index] != ' ':
							color_code = mask_lines[index][letter_index]
							new_ascii += f"${color_code}"
					new_ascii += current_line[letter_index]
				new_ascii += "\n"
	with open(source_file+"_output", 'w') as new_ascii_handle:
		new_ascii_handle.write(new_ascii)