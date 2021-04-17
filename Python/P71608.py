class Tree:
    def __init__(self, x):
        self.rt = x
        self.child = []

    def add_child(self, a):
        self.child.append(a)

    def root(self):
        return self.rt

    def ith_child(self, i):
        return self.child[i]

    def num_children(self):
        l = len(self.child)
        for node in self.child:
            l += node.num_children()
        return l

class Pre(Tree):
    def preorder(self):
        R = [self.rt]
        for node in self.child:
            R += node.preorder()
        return R