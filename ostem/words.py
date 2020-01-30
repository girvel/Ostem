import json

from ostem.meaning import Meaning
from ostem.transcription import transcribe


class Word:
    def __init__(self, text, meanings, note, basics=None):
        self.text = text
        self.meanings = meanings
        self.note = note
        self.basics = basics if basics else None

    def short_article(self):
        return '{0} ({1})'.format(
            self.text,
            self.meanings[0].value
        )

    def article(self, alphabet):
        return '{0} [{1}] - {2}.{3}{4}'.format(
            self.text,
            transcribe(self.text, alphabet),
            ', '.join(str(m) for m in self.meanings),
            f' {self.note}.' if self.note else '',
            (' Секв. из '
             + ', '.join(
                        get(a, all_words).short_article()
                        if get(a, all_words) else a
                        for a in self.basics) + '.'
             )
            if self.basics else ''
        )

    def __repr__(self):
        return f'<Word `{self.text}`>'


def load_words(path):
    with open(path, encoding='UTF-8') as f:
        return [Word(
            a["text"],
            [Meaning(**m) for m in a["meanings"]],
            a["note"],
            a.get("basics")
        ) for a in json.load(f)]


atoms = load_words('../assets/atoms.json')
words = load_words('../assets/words.json')

all_words = atoms + words


def get(word, list_, default=None):
    l = [a for a in list_ if a.text == word]
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
