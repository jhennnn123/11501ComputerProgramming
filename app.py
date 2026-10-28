from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name="Jhen12345678")

@app.route("/math")
def math():
    return "Hello, 123!"

@app.route("/html_tags")
def html_tags():
    return render_template("html_tags.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)