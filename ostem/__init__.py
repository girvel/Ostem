from ostem.atom import reduce
from ostem.transcription import classic_alphabet


if __name__ == '__main__':
    while True:
        print('\n\n'.join(a.article(classic_alphabet) for a in reduce(input(), default=tuple())))
