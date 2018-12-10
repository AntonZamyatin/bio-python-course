'''Task 9.'''
import os


class FileSystemError(Exception):
    ''' Class for errors in filesystem module '''
    def __init__(self, msg=None):
        super(FileSystemError, self).__init__(msg)


class FSItem(object):
    ''' Common class for OS items OS: Files and Directories '''

    def __init__(self, path):
        ''' Creates new FSItem instance by given path to file '''
        self.path = os.path.normpath(path)
        self.item_type = None

    def rename(self, newname):
        ''' Renames current item
                raise FileSystemError if item does not exist
                raise FileSystemError if item "newname" already exists '''
        if os.path.exists(self.path):
            if os.path.exists(os.path.split(self.path)[0] + '\\' + newname):
                raise FileSystemError("item with name {0} already exists".
                                      format(newname))
            else:
                self.path = os.path.split(self.path)[0] + '\\' + newname
        else:
            raise FileSystemError("{0} item not exists".
                                  format(self.path))

    def create(self):
        ''' Creates new item in OS
                raise FileSystemError if item with such path already exists '''
        if os.path.exists(self.path):
            raise FileSystemError("{0} already exists".
                                  format(self.path))
        else:
            if self.item_type == 'file' or not self.item_type:
                open(self.path, 'a').close()
            elif self.item_type == 'dir':
                os.makedirs(self.path)

    def getname(self):
        ''' Returns name of current item '''
        return os.path.split(self.path)[1]

    def isfile(self):
        ''' Returns True if current item exists and current item is file,
        False otherwise '''
        return os.path.isfile(self.path)

    def isdirectory(self):
        ''' Returns True if current item exists and current item is directory,
        False otherwise '''
        return os.path.isdir(self.path)


class File(FSItem):
    ''' Class for working with files '''

    def __init__(self, path):
        ''' Creates new File instance by given path to file
        raise FileSystemError if there exists directory with the same path '''
        if os.path.isdir(path):
            raise FileSystemError("{0} is a directory".
                                  format(os.path.normpath(path)))
        else:
            super(File, self).__init__(path)
            self.item_type = "file"

    def __len__(self):
        ''' Returns size of file in bytes
        raise FileSystemError if file does not exist '''
        if os.path.exists(self.path):
            return os.path.getsize(self.path)
        else:
            raise FileSystemError("{0} file not exists".
                                  format(self.path))

    def getcontent(self):
        ''' Returns list of lines in file (without trailing end-of-line)
                raise FileSystemError if file does not exist '''
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                return list(map(lambda x: x.strip(), f.readlines()))
        else:
            raise FileSystemError("{0} file not exists".
                                  format(self.path))

    def __iter__(self):
        ''' Returns iterator for lines of this file
                raise FileSystemError if file does not exist '''
        if os.path.exists(self.path):
            with open(self.path) as f:
                self.strings_list = f.readlines()
            self.iter_index = 0
            return self
        else:
            raise FileSystemError("{0} file not exists".
                                  format(self.path))

    def __next__(self):
        if self.iter_index < len(self.strings_list):
            x = self.strings_list[self.iter_index].strip()
            self.iter_index += 1
            return x
        else:
            raise StopIteration


class Directory(FSItem):
    ''' Class for working with directories '''

    def __init__(self, path):
        ''' Creates new Directory instance by given path
        raise FileSystemError if there exists file with the same path '''
        if os.path.isfile(path):
            raise FileSystemError("{0} is a file".
                                  format(os.path.normpath(path)))
        else:
            super(Directory, self).__init__(path)
            self.item_type = "dir"

    def items(self):
        ''' Yields FSItem instances of items inside of current directory
                raise FileSystemError if current directory does not exists '''
        if os.path.exists(self.path):
            for name in os.listdir(self.path):
                yield FSItem(self.path + '\\' + name)
        else:
            raise FileSystemError("{0} directory not exists".
                                  format(self.path))

    def files(self):
        ''' Yields File instances of files inside of current directory
                raise FileSystemError if current directory does not exists '''
        if os.path.exists(self.path):
            for name in os.listdir(self.path):
                if os.path.isfile(self.path + '\\' + name):
                    yield File(self.path + '\\' + name)
        else:
            raise FileSystemError("{0} directory not exists".
                                  format(self.path))

    def subdirectories(self):
        ''' Yields Directory instances of directories inside of current directory
        raise FileSystemError if current directory does not exists '''
        if os.path.exists(self.path):
            for name in os.listdir(self.path):
                if os.path.isdir(self.path + '\\' + name):
                    yield Directory(self.path + '\\' + name)
        else:
            raise FileSystemError("{0} directory not exists".
                                  format(self.path))

    def filesrecursive(self):
        ''' Yields File instances of files inside of this directory,
                inside of subdirectories of this directory and so on...
                raise FileSystemError if directory does not exist '''
        if os.path.exists(self.path):
            for file in self.files():
                yield file
            for dir in self.subdirectories():
                for file in dir.files():
                    yield file
        else:
            raise FileSystemError("{0} directory not exists".
                                  format(self.path))

    def getsubdirectory(self, name):
        ''' Returns Directory instance with subdirectory of current directory
        with name "name" raise FileSystemError if item "name" already exists
        and item "name" is not directory'''
        if os.path.exists(self.path + '//' + name):
            return Directory(self.path + '//' + name)
        else:
            raise FileSystemError("{0} directory not exists".
                                  format(self.path + '//' + name))
