import os
import pathlib
import shutil


project_root = pathlib.Path(__file__).parent.parent.resolve() 


class SomeStorageLibrary:

    def __init__(self) -> None:
        print('Instantiating database library...')

    def load_csv(self, filename: str) -> None:
        print(f'Loading the following file to storage medium: {filename}')
        shutil.move(filename, os.path.join(project_root, 'data', 'destination'))
        print('Load completed!')
