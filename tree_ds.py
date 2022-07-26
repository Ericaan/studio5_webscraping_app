from anytree import NodeMixin, RenderTree

class Tree_ds(NodeMixin):
    def __init__(self, name, input1, input2, parent=None, children=None):
        super(Tree_ds, self).__init__()
        self.name = name
        self.input1 = input1
        self.input2 = input2
        self.parent = parent
        if children:
            self.children = children