from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("./index.html")


@app.route("/run")
def run():
    print("Run button was clicked")
    return "Running"


@app.route("/stop")
def stop():
    print("Stop button was clicked")
    return "Stopped"


if __name__ == "__main__":
    app.run()
