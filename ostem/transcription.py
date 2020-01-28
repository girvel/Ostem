import json


global_alphabet = {
    "'": "ʲ"
}

with open('../assets/alphabets/classic.json', encoding='UTF-8') as f:
    classic_alphabet = {**json.load(f), **global_alphabet}

with open('../assets/alphabets/ipa_to_russian.json', encoding='UTF-8') as f:
    ipa_to_russian = {**json.load(f)}


def transcribe(word, alphabet):
    return (alphabet.get(word[0], word[0]) + transcribe(word[1:], alphabet)) if word else word
