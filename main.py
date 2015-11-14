from flask import Flask, render_template, g
import sqlite3
import group

app = Flask(__name__)

conn = sqlite3.connect('user_db.db')
c = conn.cursor()
'''
c.execute("CREATE TABLE users
                 (group_id text, user_id integer)")

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


if __name__ == "__main__":
    app.run()