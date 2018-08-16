# Markov Text Generator

Generates text based on some input text. Currently designed to parse Hamlet and
write like any of the characters. Downloads the text from the internet.

## Installation

Requires python 3.x, you'll need to install the dependencies (I would suggest a
virtual env).

    pip install -r requirements.txt

## Example Usage

    import hamlet
    import markov

    all_speeches = hamlet.load()
    example_speech = markov.write_like_this(all_speeches["HAMLET"])

## Sample Output

### Hamlet

> aside nay speak 'sblood there seek out at a divinity that ever the ominous horse hath made am easier to make the king's mess 'tis not shame to note that i for the death have it is fashion i' the mean my word for god's love make known now my weakness and thereabout of his visage together

### Ophelia

> could beauty my lord you now receive them

### Laertes

> think it my father comes a woodcock to my lord
