import sqlite3


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
    cur.execute("SELECT (?) from groups", (group_id,))
    con.commit()
    con.close()