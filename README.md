# Markov Text Generator

Generates text based on some input text. Currently designed to parse Hamlet and
write like any of the characters. Downloads the text from the internet.

## Installation

Requires python3, best run inside a virtualenv.

    # requires python3
    # setup virtualenv
    python3 -m venv ./env
    # activate env
    . ./env/bin/activate
    # install requirements
    pip install -r requirements.txt

## Usage

### Command line usage

    from sources.shakespeare import load, plays
    from markov import write_like_this

    speeches = load(plays["hamlet"])
    speech = write_like_this(speeches["HAMLET"])

### Running a server

You can run a server to generate speeches from your favourite characters! Fire
it up as follows:

    python application.py

#### List plays

    GET /plays

#### List characters

    GET /characters/<play>

#### Generate a speech

    GET /speech/<play>/<character>

## Sample Output

### Hamlet

> aside nay speak 'sblood there seek out at a divinity that ever the ominous horse hath made am easier to make the king's mess 'tis not shame to note that i for the death have it is fashion i' the mean my word for god's love make known now my weakness and thereabout of his visage together

### Ophelia

> could beauty my lord you now receive them

### Laertes

> think it my father comes a woodcock to my lord
