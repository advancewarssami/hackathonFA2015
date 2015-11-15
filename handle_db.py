import sqlite3
import backend


def execute_query(query, args=()):
    con = sqlite3.connect('user_db.db')
    cur = con.cursor()
    cur.execute(query, args)
    con.commit()
    con.close()


def insert_group(group):
    con = sqlite3.connect('user_db.db')
    cur = con.cursor()
    cur.execute("INSERT INTO groups VALUES (?, ?)", (group.name, group.serialize_good_times()))
    con.commit()
    con.close()


def query_for_group_times(group_id):
    con = sqlite3.connect('user_db.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM groups WHERE group_id = VALUES (?)", (group_id,))
    con.commit()
    con.close()
    all_items = cur.fetchall()
    ret = backend.Group.load(all_items)
    return ret.get_available_times()


def create_group(group_name):
    new_group = backend.Group(group_name)
    insert_group(new_group)


def create_user(user_name, group_name):
    new_user = backend.User(user_name)
    new_user.set_group(group_name)
