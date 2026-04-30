from PyQt6.QtWidgets import *
from pathlib import Path

#shutil.move(current folder, desired folder)
class Sorter:
    def __init__(self) -> None:
        """Creates variables that will be used consistently"""
        self.file_groups = []
        self.__folder = None
        self.files = []
    def create_and_organize(self, path) -> None:
        """using pathlib's Path to make the selected folder able to be worked with.
        also makes a list called files which stores the files that will be organized.
        """
        self.__folder = Path(path)
        self.files = [file for file in self.__folder.iterdir() if file.is_file()]

        """gets the extension of the file to group them up in the future"""
        for file in self.files:
            file_extension = file.suffix.lower()
            if file_extension not in self.file_groups:
                self.file_groups.append(file_extension)
        print(self.file_groups)

    def sort(self) -> None:
        """creates the folders based on the extensions of the files,
        if they don't have extensions they get put in the miscellaneous folder
        """
        for file_extension in self.file_groups:
            new_folder = self.__folder / file_extension
            misc_folder = self.__folder / "Miscellaneous"
            if file_extension == "" and not misc_folder:
                misc_folder.mkdir()
            elif not new_folder.exists():
                new_folder.mkdir()
        
