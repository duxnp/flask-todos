import re
from datetime import datetime
from flask import render_template

from . import main

@main.route("/")
def index():
    return render_template('index.html')

@main.route("/hello/<name>")
def hello(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now

    return render_template('hello.html', clean_name=clean_name, formatted_now=formatted_now)

@main.route("/semantic")
def semantic():
    return render_template('semantic.html')