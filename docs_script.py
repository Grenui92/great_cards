import pathlib
def replacedyll():
    direct = pathlib.Path('docs/build/html/')
    for ex in direct.rglob('*'):
        if ex.is_dir():
            continue
        if ex.is_file() and ex.name.endswith('.html'):
            new_file = []
            with open(ex, 'r+') as f:
                text = f.readlines()
                f.seek(0)
                print(text)
                for k in text:

                    if '_static' in k:
                        k = k.replace('_static', 'static')
                    new_file.append(k)
                f.writelines(new_file)
                f.truncate()

                        
if __name__ == '__main__':
    replacedyll()