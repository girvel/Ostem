from ostem.translation import translate, from_ostem, translate_word, from_russian

if __name__ == '__main__':
    cmd = ''

    actions = {
        ':t': lambda: print(translate(input())),
        ':fo': lambda: print(from_ostem(input())),
        ':fr': lambda: print(from_russian(input())),
    }

    while cmd != ':q':
        try:
            actions.get(cmd := input(), lambda: print('Wrong command'))()
        except Exception as ex:
            print(ex)
