class elfFolder:
    def __init__(self, name, parent):
        self.name = name
        self.children = []
        # self.children = children
        # self.files = files
        self.parent = parent
        if parent is not None:
            parent.addChild(name)

    def newFolder(self, name, parent):
        self.name = name
        self.parent = parent

    def addChild(self, children):
        self.children += children

    def addFile(self, elfFile):
        self.children.append(elfFile)

    def size(self):
        sum = 0
        for child in self.children:
            if child is elfFile:
                sum += child.size
            elif child is elfFolder:
                sum += child.size()
        return sum
        #print(f"The directory {self.name} has a size of {sum}")


class elfFile(elfFolder):
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        if parent is not None:
            parent.addFile(name)

    def newFile(self, size, name):
        self.name = name
        self.size = size


def main():
    root = elfFolder("/", None)
    a = elfFolder("a", parent=root)
    file1 = elfFile("file1", 949, a)
    file2 = elfFile("file2", 420, a)
    file3 = elfFile("file3", 666, root)
    print(root.size())
    print(type(a))


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
