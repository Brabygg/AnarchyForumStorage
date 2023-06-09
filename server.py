from flask import Flask
from markupsafe import escape
from main import load, save
import json

server = Flask(__name__)

@server.route("/load/<id>")
def loadPost(id):
    data = load(id)
    return data


@server.route("/save/<t>/<b>/<a>")
def writePost(t, b, a):
    save(t, b, a)
    return "Entry saved"
