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
        self.prefix = ''
        self.stop = False
        self.current_command = None
        print()

    def read_command(self):
        self.prefix = self.user + '@biosh ' + self.current_folder.path + '\n$'
        print(self.prefix, end=' ')
        s = input()
        if s:
            self.current_command = Command(s)
        else:
            raise Exception

    def command_exec(self):
        command = getattr(self, self.current_command.command)
        if command:
            command(* self.current_command.args)
        if not self.stop:
            self.prefix = self.user + '@biosh ' +\
                          self.current_folder.path + '\n$'

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
        print()

    def cd(self, dir):
        if not os.path.isabs(dir):
            dir = os.path.join(self.current_folder.path, dir)
        if dir == '.':
            return
        if os.path.exists(dir) and os.path.isdir(dir):
            self.current_folder = FSI.Directory(dir)
        else:
            print("There is no such directory")
        print()

    def cat(self, file_path):
        if not os.path.isabs(file_path):
            file_path = os.path.join(self.current_folder.path, file_path)
        if not os.path.exists(file_path):
            print("File doesnt exist")
            print()
            return
        if not os.path.isfile(file_path):
            print("This is not a file")
            print()
            return
        with open(file_path, "r") as file:
            for string in file.readlines():
                print(string, end='')
        print()

    def clear(self):
        os.system('cls')

    def head(self, file_path, *args):
        if not os.path.isabs(file_path):
            file_path = os.path.join(self.current_folder.path, file_path)
        if not os.path.exists(file_path):
            print("File doesnt exist")
            print()
            return
        if not os.path.isfile(file_path):
            print("This is not a file")
            print()
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
        print()

    def tail(self, file_path, *args):
        if not os.path.isabs(file_path):
            file_path = os.path.join(self.current_folder.path, file_path)
        if not os.path.exists(file_path):
            print("File doesnt exist")
            print()
            return
        if not os.path.isfile(file_path):
            print("This is not a file")
            print()
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
        print()

    def pwd(self):
        print(self.current_folder.path)
        print()

    def touch(self, file_path):
        if not os.path.isabs(file_path):
            file_path = os.path.join(self.current_folder.path, file_path)
        if os.path.exists(file_path):
            print("Already exists")
        else:
            file = FSI.File(file_path)
            file.create()
        print()

    def find(self, name):
        fl = self.current_folder.filesrecursive()
        for file in fl:
            if os.path.basename(file.path)[:len(name)] == name:
                print(file.path)
        print()

    def print_err(self):
        print("wrong command or arguments")
        print()

    def __getattr__(self, attr):
        print('{} is not a command'.format(self.current_command.command))
        print()
        return None


if __name__ == "__main__":
    shell = Shell()
    while not shell.stop:
        try:
            shell.read_command()
        except Exception:
            print()
            continue
        try:
            shell.command_exec()
        except TypeError:
            shell.print_err()
