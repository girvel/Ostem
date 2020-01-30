import json
from tkinter import Tk, Label, Entry, Button, END, messagebox

from ostem.meaning import Meaning
from ostem.transcription import classic_alphabet
from ostem.words import Word, get, words, atoms

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

counter = Label(master)

counter.refresh = lambda: counter.configure(text=f'{len(words) + len(atoms)} words')
counter.refresh()


def push():
    l = words if basics_entry.get() else atoms

    if any(w.text == word_entry.get() for w in l):
        messagebox.showinfo('Wrong input', f'The word "{word_entry.get()}" is already in the list')
        return

    if any(c not in classic_alphabet for c in word_entry.get()):
        messagebox.showinfo('Wrong input', f'The word "{word_entry.get()}" contains wrong characters')
        return

    if any(not get(b, words + atoms) for b in basics_entry.get().split(', ')):
        messagebox.showinfo('Wrong input', f'There are some unknown sequencing sources')
        return

    l.append(
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

    counter.refresh()


push_button = Button(master, command=push, text='Push')
push_button.pack()
counter.pack()


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
