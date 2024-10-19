# I ran my basic site through this: https://codebeautify.org/minify-html
# for these results
import sys

# Here is a useful gist that has minifying html and everything else:
# https://gist.github.com/waterrmalann/7318e61de34341a3c3bf9964e144c547

# Here is a javascript minifyier for python:
# https://github.com/ndparker/rjsmin

# https://stackoverflow.com/questions/6150108/how-to-pretty-print-html-to-a-file-with-indentation
from bs4 import BeautifulSoup as bs
import os
import fs

# TODO Hook this up to Tkintker test GUI

# This works!
# https://stackoverflow.com/a/47259051

# TODO Why is there two of these?
def prettify_html(html_file):
    if os.path.exists(html_file):
        with open (html_file) as f:
            htmlParse = bs(f, "html.parser")
            return htmlParse.prettify()
    else:
        print("Path not found!")

def print_prettify_html(html_file):
    if os.path.exists(html_file):
        with open (html_file) as f:
            htmlParse = bs(f, "html.parser")
            print(htmlParse.prettify())
    else:
        print("Path not found!")

def output_beautify(intput_file, output_file):
    with open (intput_file, "w") as f:
        f.write(prettify_html(output_file))

# Remove these for GUI
# def main():
#     value = input("What would you like to do? Print Prettify html (1), Output Beautify html (2), Quit(3)?: ")
#
#     if value == "1":
#         print_prettify_html(html_file_path)
#     elif value == "2":
#         output_beautify()
#     elif value == "3":
#         print("Exiting!")
#         sys.exit(0)
#
# if __name__ == '__main__':
#     main()