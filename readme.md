# ASCII Colorizer Assistant
### A simple Python script for adding color for [fastfetch](https://github.com/fastfetch-cli/fastfetch) sources

This script allows the creation of a numbered color guide from an ASCII art text file. This can then be merged back together, allowing easier complex coloring for fastfetch.

#### Usage:
```python main.py [options] path/to/ascii_art.txt```
#### Options:
- `-n, --number`: Generate a numeric mask with non-zero numeric indexes for each unique symbol
- `-o, --override`: Force mask generation or merge, even if the file already exists
- `-m, --merge`: Merges an existing mask with the source ASCII art file

Project established in part of [Boot.dev](https://www.boot.dev?bannerlord=flamesoulis)'s course work.

## To Do
- [x] Complete merge_mask function
- [x] Be more compliant about file extensions
- [x] Address line size comparisons
- [ ] Use argparse
  * Simplifies validate_param
  * No point re-writing the wheel