import tkinter as tk
from pathlib import Path
from tkinter import ttk, messagebox, Entry
from tkcalendar import Calendar
import os

from password_hasherSHA512 import hash_password, verify_password
from yt_thumbnail_downloader import download_thumbnail


# from tab_test import show_message_box, show_error_message, show_continue_dialog, print_test, welcome_message

# https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes

# I need to use classes in python more, they seem very useful.

# TODO Swtich tab_test.py to using classes like this.

def show_error_message():
    messagebox.showerror("Error test", "Error, mistake made.")

# Test pages
# class MainPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Main Page")
#         label.pack(padx=10, pady=10)
#
#         # We use the switch_window_button in order to call the show_frame() method as a lambda function
#         switch_window_button = tk.Button(
#             self,
#             text="Go to the Side Page",
#             command=lambda: controller.show_frame(SidePage)
#         )
#
#         welcome_label = ttk.Label(self, text="Welcome to the Main tab.")
#         welcome_label.pack(side="top", fill=tk.X)
#
#         # test_label = ttk.Label(self, text="Test")
#         # test_label.pack(side="top", fill=tk.X)
#
#         # Not sure how to get this working with the classes yet.
#         # quit_button = tk.Button(self, text="Quit", command=self.destroy)
#         # quit_button.pack(side="top", fill=tk.X)
#
#         switch_window_button.pack(side="bottom", fill=tk.X)
#
# class SidePage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="This is the Side Page")
#         label.pack(padx=10, pady=10)
#
#         switch_window_button = tk.Button(
#             self,
#             text="Go to the Completion Screen",
#             command=lambda: controller.show_frame(CompletionScreen),
#         )
#         switch_window_button.pack(side="bottom", fill=tk.X)
#
#
# class CompletionScreen(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#
#
#         label = tk.Label(self, text="Completion Screen, we did it!")
#         label.pack(padx=10, pady=10)
#         # I'm not exactly sure how this lambda is working.
#         switch_window_button = ttk.Button(
#             self, text="Return to menu", command=lambda: controller.show_frame(MainPage)
#         )
#         switch_window_button.pack(side="bottom", fill=tk.X)

# End test pages

# New

######
# Register tab
######

class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.user_name_var = tk.StringVar()
        self.password_var = tk.StringVar()

        # TODO Fix this to work.
        # Save to text file for now with hashed password
        def register():
            # This should be in the same directory
            login_file = "logins.txt"
            login_file_path = Path(f"{login_file}")

            if self.user_name_var.get() and self.password_var.get():
                # Add username and hashed password to a text file

                # Make sure the username and password exist
                if not login_file_path.exists():
                    # Create file and add to it if it doesn't exist.
                    with open(login_file, 'x') as f:
                        f.write(f"Username: {self.user_name_var.get()}\n")

                        f.write(f"Password: {self.password_var.get()}\n")
                        f.write(f"Hashed password: {hash_password(self.password_var.get())}\n")

                    print(
                        f"Created file {login_file} and added the username, clear text password and hashed password to it.")
                # Overwrite existing file if it exists
                else:
                    with open(login_file, 'w') as f:
                        f.write(f"Username: {self.user_name_var.get()}\n")

                        f.write(f"Password: {self.password_var.get()}\n")
                        f.write(f"Hashed password: {hash_password(self.password_var.get())}\n")

                    print(
                        f"Added username, clear text password, and hashed password to existing \"{login_file}\" file.")

            # Error out if they don't exist
            else:
                print("Error, you need to specify a username and password!")


        label = tk.Label(self, text="Register page")
        # label.pack(padx=10, pady=10)
        label.place(relx=0.5, rely=0.1, anchor="center")
        # label.grid(column=0, row=0, padx=10, pady=5)

        username_label = ttk.Label(self, text="Username: ")
        # username_label.pack(padx=10, pady=10, side=tk.LEFT)
        username_label.grid(column=3, row=1, padx=10, pady=5)

        user_name_entry = ttk.Entry(self, textvariable=self.user_name_var)
        user_name_entry.grid(column=4, row=1, padx=10, pady=5)

        # username_entry.pack(padx=10, pady=10, side=tk.LEFT)


        password_label = ttk.Label(self, text="Password: ")
        password_label.grid(column=3, row=2, padx=10, pady=5)
        # password_label.pack(padx=10, pady=10, side=tk.LEFT)

        password_entry = ttk.Entry(self, textvariable=self.password_var, show="*")
        password_entry.grid(column=4, row=2, padx=10, pady=5)
        # password_entry.pack(padx=10, pady=10, side=tk.LEFT)

        # Register test
        register_button = ttk.Button(self, text="Register", command=register)
        register_button.grid(column=4, row=3, padx=10, pady=5)
        # register_button.pack(padx=10, pady=10, side=tk.RIGHT)

######
# End register tab
######

######
# Login tab
######

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # TODO Figure out how to center this without screwing up the other elements

        # https://stackoverflow.com/questions/48306487/python-3-tkinter-center-label-text
        label = tk.Label(self, text="Login page")
        # This seems to work
        label.place(relx=0.5, rely=0.1, anchor="center")
        # label.grid(column=0, row=0, padx=10, pady=5)

        # label.pack(padx=10, pady=10)

        self.user_name_var = tk.StringVar()
        self.password_var = tk.StringVar()

        def login():
            user_name = self.user_name_var.get()
            password = self.password_var.get()

            # SHA512 hash of the password "test"
            tmp_password_hash = "64c6167a48f9d45f2da8073ba569d605ac6d12cece7aeec7b38a4db4bf782051f15554c83de5c757c0ae1db563c90c163f3132c869cacdf03bb2fe94ac62321c455e480fcf7fb7791acb2d2945c87b4171e5599c38d3691fcb957185d8fc9bc1"
            # Print the values
            # TODO Figure out how to store these in a text file, hashing the password,
            #  eventually figure out how to hook this up to a Mariadb or MySql DB.
            print(f"Username: {user_name}")
            print(f"Password (Hashed): {hash_password(password)}")
            # Possibly remove the clear password from this, it's only really for testing and should never be used in production.
            # if debug_mode:
            #     print(f"Password (Clear): {password}")

            # Verify the password with the above hash, this is only needed for auth and i'll disable it for now.

            # TODO Figure out how to do this verifying from the text file

            # Local directory
            login_file = "logins.txt"
            login_file_path = Path(f"{login_file}")
            if not login_file_path.exists():
                with open(login_file, 'x') as f:
                    f.readline()

            if verify_password(tmp_password_hash, password):
                print("Password is valid.")
            else:
                print("Password is invalid.")
            # print(f"Is password valid: {verify_password(tmp_password_hash, password)}")

            # Reset the values
            self.user_name_var.set("")
            self.password_var.set("")

        username_label = ttk.Label(self, text="Username: ")
        username_label.grid(column=3, row=1, padx=10, pady=5)
        # username_label.pack(padx=10, pady=10)
        password_label = ttk.Label(self, text="Password: ")
        password_label.grid(column=3, row=2, padx=10, pady=5)
        # password_label.pack(padx=10, pady=10)

        user_name_entry = ttk.Entry(self, textvariable=self.user_name_var)
        user_name_entry.grid(column=4, row=1, padx=10, pady=5)
        # user_name_entry.pack(padx=10, pady=10)
        password_entry = ttk.Entry(self, textvariable=self.password_var, show="*")
        password_entry.grid(column=4, row=2, padx=10, pady=5)
        # password_entry.pack(padx=10, pady=10)

        # Login test
        login_button = ttk.Button(self, text="Login", command=login)
        login_button.grid(column=4, row=3, padx=10, pady=5)
        # login_button.pack(padx=10, pady=10)

######
# End login tab
######

######
# Led Controller tab
######

class LedControllerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Led Controller Page")
        label.pack(padx=10, pady=10)

######
# End led controller tab
######

######
# Test Tab
######
class TestPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # welcome_label = ttk.Label(self, text="Welcome to the test tab.")
        # welcome_label.pack(padx=10, pady=10)

        self.test_var = tk.StringVar()
        self.video_id_var = tk.StringVar()

        # https://www.tutorialspoint.com/python/tk_pack.htm
        # This is how to get stuff to go beside of everything with pack
        # This might be useful for later.
        test_button1 = ttk.Button(self, text="Test #1")
        test_button1.pack(padx=10, pady=10)

        test_label1 = ttk.Label(self, text="Test label")
        test_label1.pack(padx=10, pady=10)

        def submit():
            # Get the values
            test_var = self.test_var.get()

            # Print the values
            if test_var:
                print(f"Test Var: {test_var}")

            # Reset the values
            self.test_var.set("")
            if os.name == "windows":
                os.system("clear")

        # Moved video thumbnail downloader into this.
        def download_video_thumbnail():
            video_id = self.video_id_var.get()
            # thumbnail_url = "https://img.youtube.com/vi/" + video_id + "/maxresdefault.jpg"

            if video_id:
                print(video_id)
                download_thumbnail(video_id)
            else:
                print("No video id specified")
            self.video_id_var.set("")


        # test_label2 = ttk.Label(self, text="Test2")
        # test_label2.pack(padx=10, pady=10)

        video_id_entry = ttk.Entry(self, textvariable=self.video_id_var)
        video_id_entry.pack(padx=10, pady=10, side=tk.LEFT)

        download_thumbnail_button = ttk.Button(self, text="Download Video Thumbnail", command=download_video_thumbnail)
        download_thumbnail_button.pack(padx=10, pady=10, side=tk.LEFT)


        # This works for moving stuff to the right
        # This needs to be below the part that is doing tk.LEFT for the side.
        # test_button1 = ttk.Button(self, text="Test #2")
        # test_button1.pack(padx=10, pady=10, side=tk.RIGHT)
        #
        # test_label1 = ttk.Label(self, text="Test label")
        # test_label1.pack(padx=10, pady=10, side=tk.RIGHT)



        # https://www.activestate.com/resources/quick-reads/how-to-position-widgets-in-tkinter/
        # test = tk.Label(self, text="red", bg="red", fg="white")
        # test.pack(padx=5, pady=15, side=tk.LEFT)
        # test = tk.Label(self, text="green", bg="green", fg="white")
        # test.pack(padx=5, pady=20, side=tk.LEFT)
        #
        # test1 = tk.Label(self, text="purple", bg="purple", fg="white")
        # test1.pack(padx=5, pady=20, side=tk.LEFT)
        #

        # ttk.Button(self, text="Info message", command=show_message_box).grid(column=0, row=1, padx=10, pady=5)
        # error_msg_button = ttk.Button(self, text="Error message", command=show_error_message)
        # error_msg_button.pack(padx=10, pady=10)

        # ttk.Button(self, text="Ok/Cancel Dialog", command=show_continue_dialog).grid(column=0, row=3, padx=10, pady=5)
        #
        # # Adding padx and pady seems to add spacing to these, I set a value of 10 for x and 5 for y for now.
        # ttk.Button(self, text="Print #1", command=print_test).grid(column=0, row=4, padx=10, pady=5)
        # ttk.Button(self, text="Print #2", command=welcome_message).grid(column=0, row=5, padx=10, pady=5)
        # ttk.Button(self, text="Minify HTML").grid(column=0, row=6, padx=10, pady=5)
        # ttk.Button(self, text="Beautify HTML").grid(column=0, row=7, padx=10, pady=5)

######
# End test tab
######

#

#####
# Calendar
class CalendarPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        welcome_label = ttk.Label(self, text="Welcome to the calandar tab.")
        welcome_label.pack(padx=10, pady=10)

        # https://www.geeksforgeeks.org/create-a-date-picker-calendar-tkinter/
        cal = Calendar(self, selectmode='day',
                       year=2024, month=10,
                       day=18)

        cal.pack(pady=20)

#####

# Root window
class Windows(tk.Tk):
    # Switch view frames, Oops I had to move this in the class
    def show_frame(self, cont):
        frame = self.frames[cont]
        # Raise the current to the top
        frame.tkraise()

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Add the window title
        self.wm_title("KCNet Systems")
        self.geometry('600x400')

        # Add the tabs
        # https://stackoverflow.com/questions/72190280/how-properly-use-our-code-in-different-tabs-using-the-classes

        # This works!!
        # 10-17-2024 @ 3:38PM
        self.tabControl = ttk.Notebook(self)

        self.tabControl.pack(fill="both", expand=True)

        self.app_data = {}

        # Add more tabs here
        tab_list = [RegisterPage, LoginPage, LedControllerPage, TestPage]
        for N, F in enumerate(tab_list):
            tab = F(self.tabControl, self.app_data)
            # What exactly is this doing?
            # Oh, this just puts the tab numbers in the tabs at the top
            # self.tabControl.add(tab, text="Tab"+str(N+1))

            # I fixed this to get the names from the classes and remove the word "Page" from it.
            self.tabControl.add(tab, text=f"{F.__name__}".replace("Page", ""))

        #

        # Create a frame and assign it to the container
        container = tk.Frame(self, height=400, width=600)
        # Specify the region where the frame is packed in root.
        container.pack(side="top", fill="both", expand=True)

        # Configure the location when using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # This is the old code.
        # Create a directory of frames
        # self.frames = {}
        # We will create the frames later, but first we add the components to the dict:
        # for F in (MainPage, SidePage, CompletionScreen):
        #     frame = F(container, self)
        #
        #     # The Windows class acts as the root window for the frames
        #     self.frames[F] = frame
        #     frame.grid(row=0, column=0, sticky="nsew")

        # Use a method to switch frames
        # self.show_frame(MainPage)

        #

if __name__ == "__main__":
    testObj = Windows()
    testObj.mainloop()
