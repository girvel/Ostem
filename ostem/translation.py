from ostem.transcription import classic_alphabet, transcribe, ipa_to_russian
from ostem.words import get, reduce, words, atoms, all_words

punctuation_marks = ('.', ',', ';', '!', '?', ':', '?!', '...')


def is_upper_case(word):
    return word and word[0].isupper()

def upper_case(word):
    return word[0].upper() + word[1:]


def translate_word(text):
    uc = is_upper_case(text)

    text = text.lower()

    if new_word := get(text, all_words):
        v = new_word.meanings[0].value
    elif new_word := reduce(text):
        v = '/'.join(w.meanings[0].value for w in new_word)
    else:
        v = transcribe(transcribe(text, classic_alphabet), ipa_to_russian)

    return upper_case(v) if uc else v


def translate(text):
    result_list = []

    for word in text.split(' '):
        mark = ''
        for m in punctuation_marks:
            if word.endswith(m):
                mark = m
                word = word[:-len(m)]

        result_list.append(translate_word(word) + mark)

    return ' '.join(result_list)


def from_russian(meaning, alphabet=classic_alphabet):
    return '\n\n'.join(w.article(alphabet) for w in all_words if any(m.value == meaning for m in w.meanings))


def from_ostem(word, alphabet=classic_alphabet):
    return get(word.lower(), all_words).article(alphabet)
