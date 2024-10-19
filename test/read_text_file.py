import re
import pandas as pd


# https://stackoverflow.com/questions/67351126/finding-the-line-of-a-specific-string-and-reading-the-text-file-after-that-line
# r = re.compile(r"")
#

#
# line_counter = 0
# with open(logins_file, "r") as f_in:
#     for l in f_in:
#         line_counter += 1
#         if r.search(l):
#             break
#
# df = pd.read_csv(logins_file, skiprows=line_counter, sep=r"\s+")
# print(df)

# https://discourse.mcneel.com/t/writing-and-reading-existing-txt-file/155672
# with open('tkinter/logins.txt') as f:
#     data = f.read()
#     print(data)

logins_file = "tkinter/logins.txt"

# TODO Implement this below into the tkinter gui later, this can read the username and everything once I fix it.
username_key = "Username: "
password_key = "Password: "
hashed_password_key = "Hashed password: "
with open(logins_file, 'r') as f:
    lines = f.readlines()

for number, line in enumerate(lines, 1):
    if username_key in line:
        print(f"{username_key} is at line {number}")
    if password_key in line:
        print(f"{password_key} is at line {number}")
    if hashed_password_key in line:
        print(f"{hashed_password_key} is at line {number}")