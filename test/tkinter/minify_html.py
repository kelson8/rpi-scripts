# https://stackoverflow.com/questions/5597094/compressminimize-html-from-python
import os
import sys

from bs4 import BeautifulSoup as bs
import htmlmin

# TODO Hook this up to Tkintker test GUI

# This seems to work.
# https://stackoverflow.com/a/60098703

# TODO Why is there two of these?
def minify_html(input_file):
    if os.path.exists(input_file):
        with open (input_file) as f:
            html_minify = htmlmin.minify(f.read(), remove_all_empty_space=True)
            return html_minify
    else:
        print("Path not found!")

def print_minify_html(input_file):
    if os.path.exists(input_file):
        with open (input_file, "r") as f:
            html_minify = htmlmin.minify(f.read(), remove_all_empty_space=True)
            print(html_minify)
    else:
        print("Path not found!")

def output_minify(input_file, output_file):
    with open (input_file, "w") as f:
        f.write(minify_html(output_file))

# Remove these for GUI
# def main():
#     value = input("What would you like to do? Print Minify html (1), Output Minify html (2), Quit(3)?: ")
#
#     if value == "1":
#         print_minify_html(html_file_normal)
#         # minify_html(html_file_normal)
#     elif value == "2":
#         output_minify(html_file_path, html_file_normal)
#
#     elif value == "3":
#         print("Exiting!")
#         sys.exit(0)
#     else:
#         print("Invalid value!")
#
# if __name__ == '__main__':
#     main()