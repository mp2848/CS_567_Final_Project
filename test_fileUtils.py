import unittest
import os
import shutil
import tempfile

from fileUtils import SimpleFileManager  # Adjust the import path as needed

class TestSimpleFileManager(unittest.TestCase):
    def setUp(self):
        self.manager = SimpleFileManager()
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, 'test_file.txt')
        self.test_subdir = os.path.join(self.test_dir, 'test_subdir')

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_create_delete_file(self):
        self.manager.create_file(self.test_file)
        self.assertTrue(os.path.exists(self.test_file))
        self.manager.delete_file(self.test_file)
        self.assertFalse(os.path.exists(self.test_file))

    def test_create_delete_directory(self):
        self.manager.create_directory(self.test_subdir)
        self.assertTrue(os.path.exists(self.test_subdir))
        self.manager.delete_directory(self.test_subdir)
        self.assertFalse(os.path.exists(self.test_subdir))

    def test_rename_file(self):
        self.manager.create_file(self.test_file)
        new_file = os.path.join(self.test_dir, 'new_test_file.txt')
        self.manager.rename_file(self.test_file, new_file)
        self.assertTrue(os.path.exists(new_file))
        self.assertFalse(os.path.exists(self.test_file))

    def test_rename_directory(self):
        self.manager.create_directory(self.test_subdir)
        new_dir = os.path.join(self.test_dir, 'new_test_subdir')
        self.manager.rename_directory(self.test_subdir, new_dir)
        self.assertTrue(os.path.exists(new_dir))
        self.assertFalse(os.path.exists(self.test_subdir))

    def test_copy_file(self):
        self.manager.create_file(self.test_file)
        copy_file = os.path.join(self.test_dir, 'copy_test_file.txt')
        self.manager.copy_file(self.test_file, copy_file)
        self.assertTrue(os.path.exists(copy_file))

    def test_move_file(self):
        self.manager.create_file(self.test_file)
        new_location = os.path.join(self.test_dir, 'moved_test_file.txt')
        self.manager.move_file(self.test_file, new_location)
        self.assertTrue(os.path.exists(new_location))
        self.assertFalse(os.path.exists(self.test_file))

    def test_copy_directory(self):
        self.manager.create_directory(self.test_subdir)
        copy_dir = os.path.join(self.test_dir, 'copy_test_subdir')
        self.manager.copy_directory(self.test_subdir, copy_dir)
        self.assertTrue(os.path.exists(copy_dir))

    def test_move_directory(self):
        self.manager.create_directory(self.test_subdir)
        new_location = os.path.join(self.test_dir, 'moved_test_subdir')
        self.manager.move_directory(self.test_subdir, new_location)
        self.assertTrue(os.path.exists(new_location))
        self.assertFalse(os.path.exists(self.test_subdir))

    def test_list_files(self):
        self.manager.create_file(self.test_file)
        files = self.manager.list_files(self.test_dir)
        self.assertIn(os.path.basename(self.test_file), files)

    def test_list_subdirectories(self):
        self.manager.create_directory(self.test_subdir)
        subdirs = self.manager.list_subdirectories(self.test_dir)
        self.assertIn(os.path.basename(self.test_subdir), subdirs)

    def test_list_files_with_extension(self):
        self.manager.create_file(self.test_file)
        files_with_extension = self.manager.list_files_with_extension(self.test_dir, '.txt')
        self.assertIn(os.path.basename(self.test_file), files_with_extension)

    def test_get_file_size(self):
        self.manager.create_file(self.test_file)
        with open(self.test_file, 'w') as file:
            file.write("Sample data")  # Write some data to the file
        size = self.manager.get_file_size(self.test_file)
        self.assertGreater(size, 0)


    def test_list_files_recursive(self):
        # Create a temporary directory with a known structure
        temp_dir = tempfile.mkdtemp()
        sub_dir = os.path.join(temp_dir, 'subdir')
        os.makedirs(sub_dir)
        
        # Create a sample file in the subdirectory
        subdir_file = os.path.join(sub_dir, 'file2.txt')
        with open(subdir_file, 'w') as file:
            file.write('File 2')

        # Create file1.txt in temp_dir
        file1 = os.path.join(temp_dir, 'file1.txt')
        with open(file1, 'w') as file:
            file.write('File 1')

        # Test the list_files_recursive method
        file_manager = SimpleFileManager()
        result = file_manager.list_files_recursive(temp_dir)

        # Get the absolute file paths within sets
        expected = {
            os.path.abspath(file1),
            os.path.abspath(subdir_file)
        }

        result = {os.path.abspath(file_path) for file_path in result}

        self.assertSetEqual(result, expected)

        # Clean up the temporary directory
        shutil.rmtree(temp_dir)


if __name__ == '__main__':
    unittest.main()
