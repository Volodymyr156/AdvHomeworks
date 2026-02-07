from flask import Flask

app = Flask(__name__)
name = "Raynor"

@app.route("/")
def hi():
    return "Privet!"

@app.route("/user/<name>")
def username(name):
    return f"It's Jimmy"

if __name__ == "__main__":
    app.run(debug=True)