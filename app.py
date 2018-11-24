from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("tours.html")

@app.route("/test")
def test():
    return render_template("tours.html")
if __name__ == "__main__":
    app.run()