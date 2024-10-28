import unittest
import os
from FileSearch import search_file  # Assuming the search function is in `search_file.py`

class TestFileSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up a test directory structure."""
        os.makedirs("test_dir/subdir1/subsubdir1", exist_ok=True)
        os.makedirs("test_dir/subdir2", exist_ok=True)

        with open("test_dir/file1.txt", "w") as f:
            f.write("This is file1.")
        with open("test_dir/subdir1/file2.txt", "w") as f:
            f.write("This is file2.")
        with open("test_dir/subdir1/subsubdir1/file3.txt", "w") as f:
            f.write("This is file3.")
        with open("test_dir/subdir2/file4.txt", "w") as f:
            f.write("This is file4.")

    @classmethod
    def tearDownClass(cls):
        """Clean up the test directory structure."""
        for root, _, files in os.walk("test_dir", topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            os.rmdir(root)

    def test_file_in_root_directory(self):
        """Test if a file in the root directory is found."""
        self.assertTrue(search_file("test_dir", "file1.txt"))

    def test_file_in_subdirectory(self):
        """Test if a file in a subdirectory is found."""
        self.assertTrue(search_file("test_dir", "file2.txt"))

    def test_file_in_nested_subdirectory(self):
        """Test if a file in a deeply nested subdirectory is found."""
        self.assertTrue(search_file("test_dir", "file3.txt"))

    def test_file_not_found(self):
        """Test if the function correctly identifies a non-existent file."""
        self.assertFalse(search_file("test_dir", "non_existent.txt"))

    def test_invalid_directory(self):
        """Test if the function handles an invalid directory path."""
        self.assertFalse(search_file("invalid_dir", "file1.txt"))

if __name__ == "__main__":
    unittest.main()
