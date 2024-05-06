from flask import Flask

app = Flask(__name__)


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
