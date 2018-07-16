from anytree import Node, RenderTree
from exercises.structures.src.family_tree import FamilyTree

ft = FamilyTree()
ft.populate_family_tree()


def test_tree_root():
    assert ft.lucille.name.casefold() == 'Lucille'.casefold()


def test_children_nodes():
    assert len(ft.lucille.children) == 4


def test_maeby_is_granddaughter():
    assert ft.maeby.parent.name.casefold() == 'Lindsay'.casefold()


def test_george_michael_is_grandson():
    assert ft.george_michael.parent.name.casefold() == 'Michael'.casefold()


def test_buster_is_son():
    assert ft.buster.parent.name.casefold() == 'Lucille'.casefold()


def test_lindsay_is_daughter():
    assert ft.lindsay.parent.name.casefold() == 'Lucille'.casefold()


def test_george_oscar_is_son():
    assert ft.george_oscar.parent.name.casefold() == 'Lucille'.casefold()

