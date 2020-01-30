from ostem.transcription import classic_alphabet
from ostem.translation import translate, from_ostem, translate_word, from_russian
from ostem.words import all_words

if __name__ == '__main__':
    cmd = ''

    actions = {
        ':t': lambda: print(translate(input())),
        ':fo': lambda: print(from_ostem(input())),
        ':fr': lambda: print(from_russian(input())),
        ':d': lambda: print('\n\n'.join(w.article(classic_alphabet) for w in sorted(all_words, key=lambda w: w.text)))
    }

    while cmd != ':q':
        try:
            actions.get(cmd := input(), lambda: print('Wrong command'))()
        except Exception as ex:
            print(ex)
