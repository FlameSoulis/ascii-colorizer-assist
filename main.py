import sys, os
from ascii_colorizer_lib import *

def print_usage():
	print("ASCII Colorizer Assist Tool")
	print(f"Usage: {os.path.basename(__file__)} [options] file")
	print()
	print("Options:")
	print("-n, --number\tGenerates mask using indexes (non-zero)")
	print("-o, --override\tForces mask generation (overrides existing)")
	print("-m, --merge\tMerges an existing mask with file")

def gen_line(length):
	string = ""
	while len(string) < length:
		string += "-"
	return string

def error_msg(err_msg):
	print(err_msg)
	print(gen_line(len(err_msg)))
	print_usage()

def validate_param(param):
	return []

if __name__ == "__main__":
	# If we don't have enough arguments, explain how to use
	if len(sys.argv) < 2:
		print_usage()
		sys.exit(2)

	# Does the file exist?
	ascii_file = sys.argv[-1]
	if not os.path.exists(ascii_file):
		error_msg(f"{ascii_file} does not exist!")
		sys.exit(2)
	if not os.path.isfile(ascii_file):
		error_msg(f"{ascii_file} is not a file!")
		sys.exit(2)

	# Check the params
	USE_INDEX = False
	for i in range(1,len(sys.argv) - 1):
		valid_params = validate_param(sys.argv[i])
		if len(valid_params) == 0:
			error_msg(f"{sys.argv[i]} is not a valid parameter!")
			sys.exit(3)