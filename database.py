import sqlite3
import hashlib
import secrets
import argparse
conn = None
cursor = None


def open_and_create():
    global conn
    global cursor
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM user")
    except sqlite3.OperationalError:

        cursor.execute('''CREATE TABLE user
                     (username TEXT, password TEXT, salt TEXT,
                      PRIMARY KEY (username))''')


def save_new_username_correct(username, password):
    global conn
    global cursor
    salt = secrets.token_hex(16)
    digest = hashlib.sha256(password.encode('utf-8') +
                            salt.encode("utf-8")).hexdigest()
    cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?,?)",
                   (username, digest, salt))
    conn.commit()


def check_for_username_correct(username, password):
    global conn
    global cursor
    rows = cursor.execute("SELECT salt FROM user WHERE username=?", [username])
    salt = rows.fetchall()
    if len(salt) == 0:
        return -1
    digest = hashlib.sha256(password.encode('utf-8') +
                            salt[0][0].encode("utf-8")).hexdigest()
    rows = cursor.execute("SELECT * FROM user WHERE username=? and password=?",
                          (username, digest))
    conn.commit()
    results = rows.fetchall()
    if results:
        print("User is present, password is valid")
        return 1
    else:
        return -1