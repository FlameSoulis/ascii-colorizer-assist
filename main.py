import sys
import os
from ascii_colorizer_lib import *

USE_INDEX_NUMBERS 	= 0b0001
ALLOW_OVERRIDE 		= 0b0010
MERGE_MASK			= 0b0100

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
    # Lower everything
    param = param.lower()
    # Are we dealing with a - or --?
    if param[0:1] == "--":
        # Here comes the fun!
        match param[2:]:
            case "number":
                return USE_INDEX_NUMBERS
            case "override":
                return ALLOW_OVERRIDE
            case "merge":
                return MERGE_MASK
    elif param[0] == "-":
        # Oh boy!
        flags = 0
        for c in param[1:]:
            if c == "n":
                flags |= USE_INDEX_NUMBERS
            elif c == "o":
                flags |= ALLOW_OVERRIDE
            elif c == "m":
                flags |= MERGE_MASK
            else:
                return False
        return flags
    else:
        # Who are you?!
        return False


if __name__ == "__main__":
    # If we don't have enough arguments, explain how to use
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(2)

    # Does the file exist?
    ascii_file = sys.argv[-1]
    try:
        check_file(ascii_file)
    except Exception as e:
        error_msg(f"{ascii_file} {e}")
        sys.exit(2)

    # Check the params
    FLAGS = 0
    for i in range(1,len(sys.argv) - 1):
        valid_param = validate_param(sys.argv[i])
        if not valid_param:
            error_msg(f"{sys.argv[i]} is not a valid parameter!")
            sys.exit(3)
        FLAGS |= valid_param

    # Let's do this!
    if not (FLAGS & MERGE_MASK):
        output_file = generate_new_name(ascii_file, "mask")
        try:
            check_file(output_file)
        except Exception as e:
            if e == "is not a file":
                error_msg(f"{output_file} is not a file!")
                sys.exit(4)
        if os.path.isfile(output_file) and not (FLAGS & ALLOW_OVERRIDE):
            error_msg("Mask file already exits! Use override flag or delete manually.")
            sys.exit(4)
        generate_mask_file(ascii_file, FLAGS & USE_INDEX_NUMBERS)
    else:
        output_file = generate_new_name(ascii_file, "output")
        try:
            check_file(output_file)
        except Exception as e:
            if e == "is not a file":
                error_msg(f"{output_file} is not a file!")
                sys.exit(4)
        if os.path.isfile(output_file) and not (FLAGS & ALLOW_OVERRIDE):
            error_msg("Output file already exits! Use override flag or delete manually.")
            sys.exit(4)
        merge_mask(ascii_file)