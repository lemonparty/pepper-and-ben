# Pepper and Ben
A website to show photos from Pepper and Ben's wedding

The guts of it are a simple flask app to loop through an array of photo sources,
and some JavaScript to lazily load them on scroll.

## Installation

* clone the repo
* `mkvirtualenv pepper-and-ben`
* `pip install -r requirements.txt`
* `python pepper-and-ben.py`

You'll also need to create a file called `localsettings.py`, which controls the
debug state of the application, as well as if it should load development or
minified static assets. The file just needs the key `DEBUG`, so an example is:

    DEBUG = False

The CSS is written using SASS and JS is in es6. Both are managed with webpack.
Assuming you already have node and npm installed, run `npm install` to install
the packages required for this app.

Then to start webpack watching and compiling the files, run `npm run watch`. To
compile the minified files for use in production, run `npm run build`.
