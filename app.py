#!/usr/bin/python3
"""Main app file"""

from flask import Flask

App = Flask(__name__)

@App.route("/")
def root():
    """function opens main site"""
    return "Hello World"

@App.route("/health")
def health():
    """simple health check"""
    return "ok"

if __name__ == "__main__":
    App.run()
