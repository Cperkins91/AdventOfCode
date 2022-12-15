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
            # self.size = sum(child.size for child in self.children)
#       else:
#            self.size += child.findSize
        return self.size

    def addChild(self, children: elfFolder):
        self.children.append(children)
        self.isFile = False


'''
    @property
    def size(self) -> int:
        if self._size is None:
            self._size = sum([child.size for child in self.children])
        return self._size
'''


def main():
    root = elfFolder("/", None, None, [])
    a = elfFolder("a", root, None, [])
    b = elfFolder("b", a, None, [])
    file1 = elfFolder("file1", a, 444, [])
    file2 = elfFolder("file2", a, 69, [])
    file3 = elfFolder("file3", root,333,[])
    print(root.findSize)
    print(file1)



'''
 lines = open('cmdlines.txt', 'rt').read()
 lines = lines.split('\n')
 for line in lines:
     current = line.split()
     if current[0] == '$':
         if current[1] == cd:
'''

if __name__ == '__main__':
    main()
