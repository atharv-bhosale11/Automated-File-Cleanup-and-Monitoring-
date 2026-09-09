import os
import tempfile
from src.DirectoryHealthMonitor import DirectoryScanner


def test_invalid_directory():
    DirectoryScanner("InvalidDirectoryPath")


def test_valid_directory():
    with tempfile.TemporaryDirectory() as test_directory:
        DirectoryScanner(test_directory)


def test_empty_file():
    with tempfile.TemporaryDirectory() as test_directory:

        empty_file = os.path.join(test_directory, "empty.txt")

        with open(empty_file, "w") as f:
            pass

        DirectoryScanner(test_directory)

        assert not os.path.exists(empty_file)


def test_non_empty_file():
    with tempfile.TemporaryDirectory() as test_directory:

        normal_file = os.path.join(test_directory, "normal.txt")

        with open(normal_file, "w") as f:
            f.write("Hello World")

        DirectoryScanner(test_directory)

        assert os.path.exists(normal_file)
