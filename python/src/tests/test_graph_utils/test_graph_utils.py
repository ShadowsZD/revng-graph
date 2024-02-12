from graph_utils import graph_utils
import pytest

@pytest.fixture
def relations():
    return {
        1: [2], 
        2: [3], 
        3: []
    }

@pytest.fixture
def relations_leafless():
    return {
        1: [2], 
        2: [3], 
        3: [1]
    }

def test_search_leaf(relations):
    id, has_leaf = graph_utils.search_leaf(relations)
    assert id == 3
    assert has_leaf == True

def test_search_leaf_no_leaf(relations_leafless):
    id, has_leaf = graph_utils.search_leaf(relations_leafless)
    assert id == -1
    assert has_leaf == False

def test_remove_leaf(relations):
    relations.pop(3)
    assert relations == {
        1: [2], 
        2: [3]
    }