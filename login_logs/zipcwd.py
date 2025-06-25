import os, zipfile

def zip_current_dir(output='cwd.zip'):
    base = os.getcwd()
    files = [f for f in os.listdir(base) if os.path.isfile(f)]

    print(f'Zipping {len(files)} files from current directory...')
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i, f in enumerate(files, 1):
            zipf.write(f)
            print(f'[{i}/{len(files)}] Zipped: {f}')

if __name__ == '__main__':
    zip_current_dir()" > zipcwd.py
