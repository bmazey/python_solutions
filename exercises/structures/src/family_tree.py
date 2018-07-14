import anytree

class FamilyTree:
    def __init__(self):
        self.lucille = anytree.Node('Lucille')

    def populate_family_tree(self):

        #ex: child = Node('Child Name', parent = parent_node)

        self.george_oscar = anytree.Node('George Oscar', parent = self.lucille)
        self.michael = anytree.Node('Michael', parent = self.lucille)
        self.lindsay = anytree.Node('Lindsay', parent = self.lucille)
        self.buster = anytree.Node('Buster', parent = self.lucille)
        self.george_michael = anytree.Node('George Michael', parent = self.michael)
        self.maeby = anytree.Node('Maeby', parent = self.lindsay)
