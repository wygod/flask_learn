from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def index():
    # return "<h1> hello world </h1>"
    header = request.headers.get("User-Agent")
    return "<p> hello world, your browser is %s </h1>" % header


@app.route("/user/<name>")
def user(name):
    return "<h1> hello, %s</h1>" % name


if __name__ == "__main__":
    app.run()