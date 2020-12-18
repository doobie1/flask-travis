#!/usr/bin/python3
"""Main app file"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    """function opens main site"""
    return "Hello World"

@app.route("/health")
def health():
    """simple health check"""
    return "ok"

if __name__ == "__main__":
    app.run()
