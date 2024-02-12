from gql import gql
from gql_utils import gql_queries

def create_query_branch_history(after: str | None = None) -> gql:
        if not after:
            return gql(gql_queries.HISTORY_BRANCH_SINGLE_HEADER + 
                       gql_queries.HISTORY_BRANCH_QUERY.replace("<AFTER>", ""))
        else:
            return gql(gql_queries.HISTORY_BRANCH_FULL_HEADER +
                       gql_queries.HISTORY_BRANCH_QUERY.replace("<AFTER>", "(after: $after)"))
        
def create_query_parents(after: str | None = None) -> gql:
        if not after:
            return gql(gql_queries.QUERY_PARENTS_FIRST_HEADER + 
                       gql_queries.QUERY_PARENTS.replace("<AFTER>", ""))
        else: 
            return gql(gql_queries.QUERY_PARENTS_HEADER + 
                       gql_queries.QUERY_PARENTS.replace("<AFTER>", ", after: $after"))
        
def add_oids(current_oids: list, new_oids: list) -> list:
    """
    add new oids to current list
    """
    for commit in new_oids:
        current_oids.append(commit["oid"])