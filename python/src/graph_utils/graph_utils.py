from typing import Tuple
from graphviz import Digraph

def search_leaf(commit_relations: dict) -> Tuple[int, bool]:
    """
    search leaf node in dict and return it oid
    """
    for oid, parents in commit_relations.items():
        if not parents:
            return oid, True
        
    return -1, False

def remove_leaf(commit_relations: dict, oid: int) -> None:
    """
    remove leaf node from list
    """
    commit_relations.pop(oid)

def update_relations(commit_relations: dict, leaf_oid: int) -> None:
    """
    update relations, removing leaf node from dict
    and leaf node oid from relations
    """
    for oid, parents in commit_relations.items():
        if leaf_oid in parents:
            commit_relations[oid].remove(leaf_oid)

def is_acyclic_graph(commit_relations: dict) -> None:
    """
    check if graph is acyclic
    """
    while commit_relations:
        leaf_oid, has_leaf = search_leaf(commit_relations)
        if not has_leaf:
            return False
        remove_leaf(commit_relations, leaf_oid)
        update_relations(commit_relations, leaf_oid)
    
    return True

def create_graph_file(commit_relations: dict) -> None:
    """
    create dot file with graph info
    """
    graph = Digraph('CommitGraph')

    for oid, parents in commit_relations.items():
        graph.node(oid)
        for parent in parents:
            graph.edge(oid, parent)

    dot_source = graph.source

    with open('commit_graph.dot', 'w') as dot_file:
        dot_file.write(dot_source)