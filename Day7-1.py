from __future__ import annotations
from typing import Optional, List, Generator, Callable
from operator import ge, le


class elfFolder:
    def __init__(self, name: str, parent: Optional[elfFolder], size: Optional[int],
                 children: Optional[List[elfFolder]]):
        self.name = name
        self._size = size
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
    def size(self) -> int:
        if self._size is None:
            for child in self.children:
                if self._size is None:
                    self._size = child.size
                else:
                    self._size += child.size
        return self._size

    def addChild(self, children: elfFolder):
        self.children.append(children)
        self.isFile = False


def dir_size(elffolder: elfFolder, threshold: int, comparison: Callable
             ) -> Generator[elfFolder, None, None]:
    if not elffolder.isFile:
        if comparison(elffolder.size, threshold):  # if size < threshold
            yield elffolder
        for child in elffolder.children:  # iterate through the children
            yield from dir_size(child, threshold, comparison)


def main():
    threshold = 100000
    lines = open('cmdlines.txt', 'rt').read()
    lines = lines.split('\n')
    root = curr_dir = elfFolder(lines.pop(0).split()[-1], None, None, [])  # add the root dir
    for line in lines:
        line = line.split()
        if line[0] == '$':  # Line is a command
            if line[1] == 'cd':
                if line[2] == '..':
                    curr_dir = curr_dir.parent  # Change to last directory
                else:  # change to new dir
                    child_dir = elfFolder(line[2], curr_dir, None, [])  # add new dir
                    curr_dir = child_dir
            if line[1] == 'ls':
                pass
        if line[0].isdigit():  # line is a file:
            child_dir = elfFolder(line[1], curr_dir, int(line[0]), None)
    directories = dir_size(root, threshold, le)
    print(sum(directory.size for directory in directories))
    TOTAL_SPACE = 70000000
    REQ_SPACE = 30000000
    freeSpace = TOTAL_SPACE - root.size
    directories = dir_size(root, REQ_SPACE - freeSpace, ge) #find directories >= the space we must free
    print(min(directory.size for directory in directories)) # print the smallest dir that is req to delete


if __name__ == '__main__':
    main()
