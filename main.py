from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Test"

@app.route("/home")
def home():
    return "Home"

if __name__ == "__main__":
    app.run()