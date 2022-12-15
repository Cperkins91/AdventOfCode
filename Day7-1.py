from __future__ import annotations
from typing import Optional, List, Generator, Callable
from operator import ge, le
from functools import cached_property


class elfFolder:
    def __init__(self, name: str, parent: Optional[elfFolder], size: Optional[int],
                 children: Optional[List[elfFolder]]):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = children
        self.isFile = True
        ''' Add this if you want to add children in the init'''
        if parent is not None:
            parent.addChild(self)

    def __str__(self) -> str:
        indent, parent = "", self.parent
        while parent:
            indent += "  "
            parent = parent.parent
        stub = " ".join([indent, "-", str((self.name, self.size))])
        if self.isFile:
            return stub
        for child in self.children:
            stub += "\n" + str(child)
        return stub

    @property
    def findSize(self):
        if self.size is None:
            for child in self.children:
                if self.size is None:
                    self.size = child.findSize
                else:
                    self.size += child.findSize
        return self.size

    def addChild(self, children: elfFolder):
        self.children.append(children)
        self.isFile = False


def main():
    lines = open('cmdlines.txt', 'rt').read()
    lines = lines.split('\n')
    root = curr_dir = elfFolder(lines.pop(0).split()[-1], None, None, [])
    for line in lines:
        line = line.split()
        if line[0] == '$':  # Line is a command
            if line[1] == 'cd':
                if line[2] == '..':
                    curr_dir = curr_dir.parent  # Change to new directory
                else:
                    child_dir = elfFolder(line[2], curr_dir, None, [])
                    curr_dir.addChild(child_dir)
                    curr_dir = child_dir
            if line[1] == 'ls':
                pass
        # if line[0] == 'dir': # line is folder
        #    elfFolder(line[1], curr_dir, None, None)
        if line[0].isdigit():  # line is a file:
            child_dir = elfFolder(line[1], curr_dir, int(line[0]), None)
            #curr_dir.addChild(child_dir) #Add this if you dont want to use the
            #conditional inside the init
        print(line[0])


'''
    root = elfFolder("/", None, None, [])
    a = elfFolder("a", root, None, [])
    b = elfFolder("b", a, None, [])
    file1 = elfFolder("file1", a, 444, [])
    file2 = elfFolder("file2", a, 69, [])
    file3 = elfFolder("file3", root, 333, [])
    print(root.findSize)
    print(file1)
'''

if __name__ == '__main__':
    main()
