from flask import Flask
from flask import render_template
from localsettings import DEBUG

app = Flask(__name__)


# routes
# -----------------------------------------------------------------------------

@app.route('/')
def index_route(params={}):
    images = [{
        'id': '1',
        'orientation': 'landscape',
    }, {
        'id': '2',
        'orientation': 'landscape',
    }, {
        'id': '3',
        'orientation': 'portrait',
    }, {
        'id': '4',
        'orientation': 'portrait',
    }, {
        'id': '5',
        'orientation': 'landscape',
    }, {
        'id': '6',
        'orientation': 'landscape',
    }, {
        'id': '7',
        'orientation': 'landscape',
    }, {
        'id': '8',
        'orientation': 'landscape',
    },]

    return render_template('index.html', images=images, debug=DEBUG)


# init
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0')
