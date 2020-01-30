import json
from tkinter import Tk, Label, Entry, Button, END

from ostem.meaning import Meaning
from ostem.words import load_words, Word

atoms = load_words('../assets/atoms.json')
words = load_words('../assets/words.json')

master = Tk()
master.geometry('200x250')

Label(master, text='Word').pack()
word_entry = Entry()
word_entry.pack()

Label(master, text='Meaning').pack()
meaning_entry = Entry()
meaning_entry.pack()

Label(master, text='Basics').pack()
basics_entry = Entry()
basics_entry.pack()

Label(master, text='Note').pack()
note_entry = Entry()
note_entry.pack()


def push():
    (words if basics_entry.get() else atoms).append(
        Word(
            word_entry.get(),
            [Meaning(w, '') for w in meaning_entry.get().split(', ')],
            note_entry.get(),
            basics_entry.get().split(', ') if basics_entry.get() else None,
        )
    )

    word_entry.delete(0, END)
    meaning_entry.delete(0, END)
    note_entry.delete(0, END)
    basics_entry.delete(0, END)


push_button = Button(master, command=push, text='Push')
push_button.pack()


if __name__ == '__main__':
    try:
        master.mainloop()
    finally:
        def encode(o):
            return o.__dict__

        with open('../assets/atoms.json', encoding='UTF-8', mode='w') as f:
            json.dump(sorted(atoms, key=lambda w: w.text), f, default=encode, indent=2, ensure_ascii=False)

        with open('../assets/words.json', encoding='UTF-8', mode='w') as f:
            json.dump(sorted(words, key=lambda w: w.text), f, default=encode, indent=2, ensure_ascii=False)
