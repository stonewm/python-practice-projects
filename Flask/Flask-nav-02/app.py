from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *

app = Flask(__name__)

Bootstrap(app)

nav = Nav()

# registers the "top" menubar
nav.register_element('top', Navbar(
    View('Home', 'index'),
    Subgroup(
        'Products',
        View('Wg240-Series', 'products', product='wg240'),
        View('Wg250-Series', 'products', product='wg250'),
        Separator(),
        Text('Discontinued Products'),
        View('Wg10X', 'products', product='wg10x'),
    ),
    Link('Tech Support', 'http://techsupport.invalid/widgits_inc'),
    View('About', 'about')
))

nav.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'This is the ABOUT page'

@app.route('/products/<product>')
def products(product):
    return 'product: ' + str(product)

if __name__ == '__main__':
    app.run()