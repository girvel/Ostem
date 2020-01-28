import json

from ostem.transcription import transcribe


class Atom:
    def __init__(self, text, meaning):
        self.text = text
        self.meaning = meaning

    def article(self, alphabet):
        return '{0} [{1}] - {2}'.format(
            self.text,
            transcribe(self.text, alphabet),
            self.meaning,
        )


with open('../assets/atoms.json', encoding='UTF-8') as f:
    atoms = [Atom(**a) for a in json.load(f)]


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
