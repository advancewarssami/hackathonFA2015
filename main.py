from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/create_group")
def create_group():
    return "Create Group"


@app.route("/group")
def group():
    return render_template('group.html')


@app.route("/start")
def start():
    return render_template('start_page.html')


@app.route('/input')
def input_page():
    return render_template('input.html')


if __name__ == "__main__":
    app.run()