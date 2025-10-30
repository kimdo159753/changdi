from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('musicMenu'))

@app.route('/api/music')
def musicMenu():
    return render_template('musicMenu.html')

@app.route('/api/music/playlist')
def playlist():
    return render_template('playlist.html')

@app.route('/api/music/<title>')
def music(title):
    return render_template('music_detail.html', current_title=title)

@app.route('/api/emotion')
def emotionMenu():
    return render_template('emotionMenu.html')

@app.route('/api/emotion/today')
def today():
    return render_template('today.html')

@app.route('/api/emotion/monthly')
def monthly():
    return render_template('monthly.html')

if __name__ == '__main__':
    app.run(debug=True)