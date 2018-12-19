"""BioSH shell application"""

import FSI
import os


class Command():

    def __init__(self, command_string):
        pars_list = command_string.split()
        self.command = pars_list[0]
        self.args = pars_list[1:]


class Shell(object):

    def __init__(self):
        self.current_folder = FSI.Directory('.')
        os.system('cls')
        print("What is your name?")
        s = input()
        while len(s.split()) > 1:
            print("Must be one word")
            s = input()
        os.system('cls')
        print("This is Bioinformatics shell. \nType \"exit\" to quit")
        self.user = s
        self.prefix = self.user + '@biosh ' + self.current_folder.path + '\n$'
        self.stop = False
        print(self.prefix, end=' ')

    def read_command(self, command_string):
        self.current_command = Command(command_string)

    def command_exec(self):
        if self.current_command.command not in self.command_list.keys():
            print('{} is not a command'.format(self.current_command.command))
        else:
            self.command_list[self.current_command.command](self,
                                                    *self.current_command.args)
        if not self.stop:
            self.prefix = self.user + '@biosh ' +\
                          self.current_folder.path + '\n$'
            print()
            print(self.prefix, end=' ')

    def exit(self):
        self.stop = True
        os.system('cls')

    def ls(self):
        dl = self.current_folder.subdirectories()
        fl = self.current_folder.files()
        row_format = "{:<40}{:>15}"
        for dir in dl:
            print(row_format.format(os.path.basename(dir.path)[:40],
                  "DIRECTORY"))
        row_format = "{:<40}" + "{:>15}" * 2
        for file in fl:
            print(row_format.format(os.path.basename(file.path)[:40],
                  "FILE", os.path.getsize(file.path)))

    def cd(self, dir):
        if dir == '.':
            return
        if os.path.exists(dir) and os.path.isdir(dir):
            self.current_folder = FSI.Directory(dir)
        else:
            print("There is no such directory")

    def cat(self, file_path):
        if not os.path.exists(file_path):
            print("File doesnt exist")
            return
        if not os.path.isfile(file_path):
            print("This is not a file")
            return
        with open(file_path, "r") as file:
            for string in file.readlines():
                print(string, end='')

    def clear(self):
        os.system('cls')

    def head(self, file_path, *args):
        if not os.path.exists(file_path):
            print("File doesnt exist")
            return
        if not os.path.isfile(file_path):
            print("This is not a file")
            return
        if not args:
            with open(file_path, "r") as file:
                for string in file.readlines()[:10]:
                    print(string, end='')
        elif len(args) != 2:
            print("wrong arguments")
        elif args[0] != "-n" or not args[1].isdigit():
            print("wrong arguments")
        elif 1 <= int(args[1]):
            with open(file_path, "r") as file:
                for string in file.readlines()[:int(args[1])]:
                    print(string, end='')

    def tail(self, file_path, *args):
        if not os.path.exists(file_path):
            print("File doesnt exist")
            return
        if not os.path.isfile(file_path):
            print("This is not a file")
            return
        if not args:
            with open(file_path, "r") as file:
                for string in file.readlines()[-10:]:
                    print(string, end='')
        elif len(args) != 2:
            print("wrong arguments")
        elif args[0] != "-n" or not args[1].isdigit():
            print("wrong arguments")
        elif 1 <= int(args[1]):
            with open(file_path, "r") as file:
                for string in file.readlines()[-int(args[1]):]:
                    print(string, end='')

    def pwd(self):
        print(self.current_folder.path)

    def touch(self, file_path):
        if os.path.exists(file_path):
            print("Already exists")
        else:
            file = FSI.file(file_path)
            file.create()

    def find(self, name):
        fl = self.current_folder.filesrecursive()
        for file in fl:
            if os.path.basename(file.path)[:len(name)] == name:
                print(file.path)

    def print_err(self):
        print("wrong arguments")
        print()
        print(self.prefix, end=' ')

    command_list = {'ls': ls, 'exit': exit, 'cd': cd,
                    'cat': cat, 'clear': clear, 'head': head,
                    'tail': tail, 'pwd': pwd, 'touch': touch,
                    'find': find}


if __name__ == "__main__":
    shell = Shell()

    while not shell.stop:
        shell.read_command(input())
        try:
            shell.command_exec()
        except TypeError:
            shell.print_err()
