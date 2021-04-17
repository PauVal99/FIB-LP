from functools import reduce

class Tree:
    def __init__(self, x):
        self.rt = x
        self.child = []

    def __iter__(self):
        #F

    def addChild(self, a):
        self.child.append(a)

    def root(self):
        return self.rt

    def ithChild(self, i):
        return self.child[i]

    def num_children(self):
        l = len(self.child)
        for node in self.child:
            l += node.num_children()
        return l

t = Tree(2)
t.addChild(Tree(3))
t.addChild(Tree(4))
t.ithChild(0).addChild(Tree(5))