from gql_utils import utils
import pytest

@pytest.fixture
def current_oids():
    return [1, 2, 3]
  
def test_add_oid(current_oids):
    utils.add_oids(current_oids, [{"oid": 4}])
    assert current_oids == [1, 2, 3, 4]

def test_add_multiple(current_oids):
    utils.add_oids(current_oids, [{"oid": 4}, {"oid": 5}])
    assert current_oids == [1, 2, 3, 4, 5]

def test_add_empty(current_oids):
    utils.add_oids(current_oids, [])
    assert current_oids == [1, 2, 3]
