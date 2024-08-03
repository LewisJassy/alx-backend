#!/usr/bin/env python3
from flask import Flask, render_template
app = Flask(__name__)

"""
Simple Flask Application

This application serves a single route
, `/`, which renders the `0-index.html` template.

Usage:
    python app.py

Attributes:
    app (Flask): The Flask application instance.
"""


@app.route("/")
def index():
    """
    Index Route

    Renders the `0-index.html` template.

    Returns:
        str: The rendered HTML template.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
