import json

from ostem.meaning import Meaning
from ostem.transcription import transcribe


class Atom:
    def __init__(self, text, meanings):
        self.text = text
        self.meanings = meanings

    def article(self, alphabet):
        return '{0} [{1}] - {2}'.format(
            self.text,
            transcribe(self.text, alphabet),
            ', '.join(str(m) for m in self.meanings),
        )


with open('../assets/atoms.json', encoding='UTF-8') as f:
    atoms = [Atom(a["text"], [Meaning(**m) for m in a["meanings"]]) for a in json.load(f)]


def get_atom(word, default=None):
    l = [a for a in atoms if a.text == word]
    return l[0] if l else default


def reduce(word, default=None):
    if not word:
        return []

    for atom in atoms:
        if word.startswith(atom.text):
            rest = reduce(word[len(atom.text):], default)
            if rest != default:
                return [atom] + rest

    return default
