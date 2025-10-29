from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return "emotion to music!"

if __name__ == "__main__":
    app.run(debug=True)
