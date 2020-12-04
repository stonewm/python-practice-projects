from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    print(url_for('index'))
    return 'Index Page'


@app.route('/about')
def about():
    return 'About Page'


if __name__ == '__main__':
    print(app.url_map)
    app.run()
