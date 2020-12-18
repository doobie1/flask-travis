#!/usr/bin/python3
"""Main APP file"""

from flask import Flask

APP = Flask(__name__)

@APP.route("/")
def root():
    """function opens main site"""
    return "Hello World"

@APP.route("/health")
def health():
    """simple health check"""
    return "ok"

if __name__ == "__main__":
    APP.run()
