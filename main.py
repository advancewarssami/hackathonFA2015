<<<<<<< HEAD
from flask import Flask
=======
from flask import Flask, render_template
>>>>>>> refs/remotes/origin/master
app = Flask(__name__)

@app.route("/")
def hello():
<<<<<<< HEAD
    
=======
>>>>>>> refs/remotes/origin/master
    return "Hello World!"

@app.route("/home")
def home():
    return "Home"

if __name__ == "__main__":
    app.run()