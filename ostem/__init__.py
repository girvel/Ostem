import json

global_alphabet = {
    "'": "ʲ"
}

with open('../assets/alphabets/classic.json', encoding='UTF-8') as f:
    alphabet = {**json.load(f), **global_alphabet}


def transcribe(word, alphabet):
    return (alphabet.get(word[0], word[0]) + transcribe(word[1:], alphabet)) if word else word


if __name__ == '__main__':
    while True:
        print(transcribe(input(), alphabet))
