from ostem.atom import get_atom
from ostem.transcription import transcribe, classic_alphabet


if __name__ == '__main__':
    while True:
        print(get_atom(input()).article(classic_alphabet))
