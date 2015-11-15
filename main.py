from flask import Flask, render_template, request, make_response, redirect, url_for
from urllib.parse import urlparse, urljoin
import backend
import handle_db
app = Flask(__name__)



def build_table(group_id):
    # return group.unserialize_good_times(handle_db.query_for_good_times(group_id))
    # id = request.cookies.get('group_id')
    # return handle_db.query_for_group_times(id)
    return request.cookies.get('group_id')


@app.route("/")
def hello():
    return render_template('input.html')


@app.route("/group", methods=['POST'])
def find_group():
    group_id = request.form['group_name']
    resp = make_response(render_template('group.html', group_id=group_id))
    resp.set_cookie('group_id', group_id)
    return resp


@app.route("/group/create_group")
def create_group():
    return render_template('create_group.html')


@app.route("/group/add_user", methods=['POST'])
def add_user():
    user_name = request.form['new_member_name']
    user_times = request.form['new_member_times']
    resp = make_response(render_template('view_user.html', user_name=user_name, user_times=user_times))
    resp.set_cookie('user_name', user_name)
    return resp


@app.route("/group/create_user")
def create_user():
    return render_template("add_user.html", group_id=request.cookies.get('group_id'))


@app.route("/group/view_available_times")
def view_times():
    group_id = request.cookies.get('group_id')
    return render_template("view_available_times.html", table=build_table(group_id))


@app.route("/group/create_group/confirm_new_group", methods=['POST'])
def confirm_group():
    group_id = request.form['new_group_name']
    member = request.form['first_member']
    return render_template('group_creation_successful.html', group_name=group_id, first_member=member)


@app.route('/group/redirect')
def goto_group():
    group_id = request.cookies.get('group_id')
    return render_template('group.html', group_id=group_id)


@app.route("/start")
def start():
    return render_template('start_page.html')


@app.route('/input')
def input_page():
    return render_template('input.html')


if __name__ == "__main__":
    app.run()
