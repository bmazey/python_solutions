from anytree import Node, RenderTree

class FamilyTree:
    def __init__(self):
        self.lucille = Node('Lucille')

    def populate_family_tree(self):

        #ex: child = Node('Child Name', parent = parent_node)

        self.george_oscar = Node('George Oscar', parent = self.lucille)
        self.michael = Node('Michael', parent = self.lucille)
        self.lindsay = Node('Lindsay', parent = self.lucille)
        self.buster = Node('Buster', parent = self.lucille)
        self.george_michael = Node('George Michael', parent = self.michael)
        self.maeby = Node('Maeby', parent = self.lindsay)
