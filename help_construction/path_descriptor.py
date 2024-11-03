from pathlib import Path

class DirectoryPathDescriptor:
    def __init__(self, path):
        self.path = Path(path)
        self.validate_directory()

    def __get__(self, instance, owner):
        """get current value atr"""
        return self.path

    def __set__(self, instance, value):
        self.path  = Path(value)
        self.validate_directory()

    def is_directory(self):
        return self.path.is_dir()

    def is_exists(self):
        return self.path.exists()

    def validate_directory(self):

        if not self.is_exists() or not self.is_directory():
            raise ValueError(f"The path '{self.path}' is not a valid directory.")
