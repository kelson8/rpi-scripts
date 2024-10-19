import os.path
import sqlite3
import secrets
from _sqlite3 import Error
import time

# from enum import Enum

# Copied from PythonProjects\testing\databases\sqlite_db_passwordgen.py on local Gitea server.
# Local only link:
# https://git.internal.kelsoncraft.net/kelson8/PythonProjects/src/branch/main/testing/databases/sqlite_db_passwordgen.py

# TODO Fix this to obtain the user folder depending on which Operating System is in use.
# Use the password generator and put a random password from it into a database
# db_path= "C:\\Users\\kelson\\Documents\\coding\\testing\\databases\\"
db_name="db_test.db"

# This is finally working, now I can generate random passwords and put them into a sqlite database.
# https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta
# I needed a comma after password1

# This uses my password generator in the function below and outputs a password into a sqlite database.

# Messages enum, basically using the same concept as I did in Java for my KBP Project for Spigot MC
class Messages:
    not_implemented_message = "Not implemented yet!"

def password_gen(password_length):
    """
    Basic password generator
    :param password_length: The password length
    :return password1: The generated password
    """
    #password_length = 20
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
    password1 = ''.join(secrets.choice(characters) for i in range(password_length))

    return password1

# TODO Fix this to work
def create_database():
    print(Messages.not_implemented_message)

def delete_passwords():
    print(Messages.not_implemented_message)

def check_for_table(conn, table):
    """
    :param conn:  Connection to the database
    :param table: The table to check for
    :return:
    """
    c = conn.cursor()
    try:
        list_of_tables = c.execute("SELECT * FROM " + table)
        print("Table found")
    except Error as e:
        print(e)
    #list_of_tables = c.execute("""SELECT * FROM passwords WHERE type='table'
    #    AND tableName='passwords'; """).fetchall()

    #return list_of_tables

def create_connection(db_file):
    """
    Creates the database connection.

    :param db_file: The database to connect to.
    :return: The connection to the database.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """
    Create a new table.

    :param conn: The connection to database.
    :param create_table_sql: The table to create.
    :return project id:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def list_password_tables(conn):
    """
    List the values in the passwords table.

    :param conn: The connection to database
    """
    # Moved outside of try block
    database_table = "passwords"
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM " + database_table)

        data_list = c.fetchall()
        print('Passwords: ')
        for item in data_list:
            print(item)
    except sqlite3.OperationalError:
        print("No such table: " + database_table)

    #except Error as e:
    #    print(e)

def add_passwords(conn, passwords):
    # TODO Setup this to where it takes a table parameter also.
    """
    Adds a password into the passwords table

    :param conn: The connection to the database.
    :param passwords: The passwords to add to the table.
    :return:
    """
    sql = "INSERT INTO passwords(list) VALUES(?)"
    cur = conn.cursor()
    cur.execute(sql, (passwords,))
    conn.commit()
    return cur.lastrowid

def main():
    # TODO Set this up to create the table if it doesn't already exist.

    # Database path
    # database = db_path + db_name
    database = db_name

    conn = (create_connection(database))

    # Create tables
    if conn is not None:
        # Switched this to use the new password generator function.
        add_passwords(conn, password_gen(20))
        # list_password_tables(conn)
        print("Success!")
    else:
        print("Error! Cannot create the database connection.")

        # Add to tables


# This was the old method I was using to generate passwords in one function,
# But I didn't want to do it like that
# def create_tables():
#     conn = sqlite3.connect(db_path + db_name)
#     cursor = conn.cursor()
#     with conn:
#         conn.execute("INSERT INTO passwords(list) VALUES (?);", (password1,))
#     print("Success!")

#create_tables()
#def create_table():

# TODO Setup this to where it asks the user if they want to add to the passwords table or list passwords from it.

if __name__ == '__main__':
    # I have this test setup to list the passwords from the database.
    # database1 = db_path + db_name
    database1 = db_name
    database_table1 = "passwords"

    # Connection
    conn1 = (create_connection(database1))
    # This will list passwords from the database.
    delete_passwords()

    ####
    # Left over testing.
    ####
    # list_password_tables(conn1)
    # # This basic test prints if a table exists in the database or not.
    # # check_for_table(conn1, database_table1)
    # time.sleep(1)
    # if os.name == "nt":
    #     os.system("cls")
    # elif os.name == "posix":
    #     os.system("clear")

    # Use main for generating the passwords
    # main()
    # list_password_tables(conn1)
    # create_database()