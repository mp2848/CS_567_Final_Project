import os
import shutil

class SimpleFileManager:
    def create_file(self, filename):
        with open(filename, 'w') as file:
            pass

    def delete_file(self, filename):
        if os.path.exists(filename):
            os.remove(filename)
        else:
            raise FileNotFoundError(f"{filename} not found")

    def create_directory(self, dirname):
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        else:
            raise FileExistsError(f"{dirname} already exists")

    def delete_directory(self, dirname):
        if os.path.exists(dirname):
            shutil.rmtree(dirname)
        else:
            raise FileNotFoundError(f"{dirname} not found")

    def list_files(self, directory='.'):
        if os.path.exists(directory):
            return os.listdir(directory)
        else:
            raise FileNotFoundError(f"{directory} not found")

    def rename_file(self, old_filename, new_filename):
        if os.path.exists(old_filename):
            os.rename(old_filename, new_filename)
        else:
            raise FileNotFoundError(f"{old_filename} not found")

    def rename_directory(self, old_dirname, new_dirname):
        if os.path.exists(old_dirname):
            os.rename(old_dirname, new_dirname)
        else:
            raise FileNotFoundError(f"{old_dirname} not found")

    def copy_file(self, source, destination):
        shutil.copy2(source, destination)

    def move_file(self, source, destination):
        shutil.move(source, destination)

    def copy_directory(self, source, destination):
        shutil.copytree(source, destination)

    def move_directory(self, source, destination):
        shutil.move(source, destination)

    def get_file_size(self, filename):
        if os.path.exists(filename):
            return os.path.getsize(filename)
        else:
            raise FileNotFoundError(f"{filename} not found")

    def list_subdirectories(self, directory='.'):
        if os.path.exists(directory):
            return [subdir for subdir in os.listdir(directory) if os.path.isdir(os.path.join(directory, subdir))]
        else:
            raise FileNotFoundError(f"{directory} not found")

    def list_files_with_extension(self, directory='.', extension='.txt'):
        if os.path.exists(directory):
            return [file for file in os.listdir(directory) if file.endswith(extension)]
        else:
            raise FileNotFoundError(f"{directory} not found")

    def count_files_in_directory(self, directory='.'):
        if os.path.exists(directory):
            return len(os.listdir(directory))
        else:
            raise FileNotFoundError(f"{directory} not found")

    def list_files_recursive(self, directory='.'):
        file_list = []
        for root, _, files in os.walk(directory):
            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list

    def get_file_creation_time(self, filename):
        if os.path.exists(filename):
            return os.path.getctime(filename)
        else:
            raise FileNotFoundError(f"{filename} not found")

    def get_file_modification_time(self, filename):
        if os.path.exists(filename):
            return os.path.getmtime(filename)
        else:
            raise FileNotFoundError(f"{filename} not found")

    def get_file_access_time(self, filename):
        if os.path.exists(filename):
            return os.path.getatime(filename)
        else:
            raise FileNotFoundError(f"{filename} not found")

    def change_file_permissions(self, filename, mode):
        if os.path.exists(filename):
            os.chmod(filename, mode)
        else:
            raise FileNotFoundError(f"{filename} not found")

    # Add more file management functions as needed...

