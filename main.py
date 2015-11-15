from flask import Flask, render_template, g
import handle_db
import group
import sqlite3


app = Flask(__name__)
'''
conn = sqlite3.connect('user_db.db')
cur = conn.cursor()

cur.execute("CREATE TABLE groups
                    (group_id, group_good_times)")
'''
'''
c.execute("CREATE TABLE users
                 (group_id text, user_name, )")

c.execute("CREATE TABLE user_times
                (user_id integer, user_times text)")
'''
'''
c.execute("INSERT INTO users VALUES ('alskdfj3', 'jordan')")
conn.commit()
conn.close()

a = group.User("Jordan")
print(a.save())
'''

'''
def select_user(params=()):
    con = sqlite3.connect('user_db.db')
    cur = con.cursor()
    if params == ():
        cur.execute("select * from users")
    else:
        string = "select"
        for i in range(len(params) - 1):
            string += "%s,"
        string += "%s"
        string += "from users"
'''
'''
time_a = group.Time(1, 7, 0)
time_b = group.Time(1, 8, 0)
time_c = group.Time(1, 7, 30)
time_d = group.Time(1, 8, 30)

group_a = group.Group('groupy_group')

user_a = group.User('jma829')
user_b = group.User('jda763')


group_a.add_user(user_a)
group_a.add_user(user_b)


user_a.add_bad_time(time_a, time_b)
user_b.add_bad_time(time_c, time_d)


handle_db.insert_group(group_a)

handle_db.query_for_group_times(group_a.name)
'''




@app.route("/create_group")
def create_group():
    return render_template('create_group.html')


@app.route("/group")
def group():
    return render_template('group.html')


@app.route("/")
def start():
    return render_template('start_page.html')


@app.route('/input')
def input_page():
    return render_template('input.html')

@app.route('/group/<group_id>')
def group_page(group_name):
    pass

if __name__ == "__main__":
    app.run()