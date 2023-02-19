from flask import Flask, render_template, request, jsonify, redirect
from chat import professor
import json
from link import get_script, get_id
import sys

app = Flask(__name__)

active = {
    
}

@app.get("/")
def home():
    return render_template("index.html")

@app.route("/?search=<url>/", methods=['GET'])
def red(url):
    return redirect("/" + get_id(url))

@app.route("/<id>/", methods=["GET"])
def create_session(id):
    script = get_script(id)
    active[id] = professor(script)
    return jsonify({
        "id" : id
    })


@app.route("/<id>/", methods=["POST"])
def question(url):
    question = request.get_json().get("question")
    return jsonify({
        "message" : active[id].add_and_submit(question)
    })


if __name__ == "__main__":
    app.run()