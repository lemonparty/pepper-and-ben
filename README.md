# Pepper and Ben
_Pepper and Ben_ is a website to show photos from Pepper and Ben's wedding.

It's a simple Flask app which loops through an array of photo sources, and
uses a little JavaScript to lazily load them on scroll.

## Installation

You'll need to create a file called `localsettings.py`, which controls the
debug state of the application, as well as if it should load development or
minified static assets. The file just needs the key `DEBUG`, so an example is:

    DEBUG = False

Assuming you have python `3.7` or greater installed:
* clone the repo
* create a virtual environment with `python -m venv pepper-and-ben-venv`
* activate the virtual environment with `source pepper-and-ben-venv/bin/activate`
* install the python packages with `pip install -r requirements.txt`
* start the server (at http://localhost:5000) with `python pepper_and_ben.py`

The CSS is written using SASS, and the JS is written in es6. Both are managed
with webpack. Assuming you already have node and npm installed, run `npm install`
to install the JS packages required for this app.

Then to start webpack watching and compiling the files, run `npm run watch`. To
compile the minified files for use in production, run `npm run build`.
