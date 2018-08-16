import re
import requests
from bs4 import BeautifulSoup, element

# Structure of document is
# <a name="speech(\d+)">{speaker}</a>
# <blockquote>[<a>{text}</a>]*n</a>
# Stage directions are in <p> tags inside the blockquote (ignore them)
# Scenes are delimited by <hX> header tags
# Should be safe to find all <a.speechX>,<blockquote> pairs, and then extract
# the text within the <a> tags inside the blockquotes.

url = "http://shakespeare.mit.edu/hamlet/full.html"

author_class = re.compile("speech(\d+)")

def name_matches(tag, pattern):
    if tag.has_attr("name"):
        return pattern.match(tag["name"]) is not None
    else:
        return False

def is_author_tag(tag):
    return tag.name == "a" and name_matches(tag, author_class)

words_only = re.compile("(^|\s+)?(('?(\w+)([\-']?))+)(\s+|$)?")
def clean_speech(text):
    """There is loads of crap in these speeches"""
    return " ".join([match[1] for match in words_only.findall(text)])

def get_speech_for_author(author_tag):
    """Given an author tag, retrieve the speech (if extant)"""
    sibling = author_tag.next_sibling
    while(type(sibling) == element.NavigableString):
        sibling = sibling.next_sibling

    if sibling is not None and sibling.name == "blockquote":
        return sibling
    else:
        return None

def get_all_speeches(soup):
    """Gets all the speeches with their authors from the tree"""
    authors = [tag for tag in soup.find_all("a") if is_author_tag(tag)]
    speeches = []
    for author in authors:
        speech = get_speech_for_author(author)
        if speech is not None:
            speaker = author.string
            text = " ".join(a.string for a in speech.find_all("a"))
            speeches.append((speaker, clean_speech(text)))
    return speeches

def organise_by_author(speeches):
    """Turn a speeches-array into a dict indexed by author"""
    by_author = {}
    for (author, speech) in speeches:
        if author not in by_author:
            by_author[author] = []
        by_author[author].append(speech)
    return by_author

def load():
    """Load the speeches"""
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    return organise_by_author(get_all_speeches(soup))
