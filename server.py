from flask import Flask, render_template, make_response, redirect
from markov import write_like_this
from sources.shakespeare import plays, load

app = Flask(__name__)

cache = {}

for play in plays:
    cache[play] = load(plays[play])

def clean_name(name):
    return name.replace("_", " ").title()

@app.route("/")
def index():
    return redirect("/plays")

@app.route("/plays")
def list_plays():
    """List all the plays"""
    names = [clean_name(name) for name in plays.keys()]
    return render_template("plays_list.html", plays=sorted(names))

@app.route("/characters/<play>")
def list_characters(play):
    """List all the characters in a play"""
    if play not in cache:
        return make_response("no such play", 404)

    names = [clean_name(name) for name in cache[play].keys()]
    return render_template("characters_list.html", play=clean_name(play), characters=sorted(names))

@app.route("/speech/<play>/<character>")
def generate_speech(play, character):
    """Generate speech for a given character"""
    title = play.lower()
    speaker = character.upper()

    if title not in cache:
        return make_response("no such play", 404)

    speeches = cache[title]

    if speaker not in speeches:
        return make_response("no such character", 404)

    text = write_like_this(speeches[speaker])
    return render_template("speech.html", play=clean_name(title), character=clean_name(character), text=text)
