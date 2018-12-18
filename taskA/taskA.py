"""BioSH shell application"""

import FSI
import os

user = "Enzo"
os.system('cls')
print("This is Bioinformatics shell. \nType \"exit\" to quit")
print(user+'@biosh$', end=' ')
comand_string = input()

def ls():
    d = FSI.Directory(".")
    print(list(map(lambda x: x.path, d.items())))

comand_list = {'ls': ls}

while comand_string != "exit":
    comand = comand_string.split()[0]
    print(comand)
    comand_list[comand]()
    print(user+'@biosh$', end=' ')
    comand_string = input()
