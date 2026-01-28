from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Feature Brandon App funcionando"

if __name__ == "__main__":
    app.run(debug=True)
