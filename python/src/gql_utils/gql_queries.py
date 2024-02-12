HISTORY_BRANCH_SINGLE_HEADER = """
query getHistorySingle($owner: String!, $name: String!) {
"""

HISTORY_BRANCH_FULL_HEADER = """
query getHistorySingle($owner: String!, $name: String!, $after: String!) {
"""

HISTORY_BRANCH_QUERY = """
   repository(owner: $owner, name: $name) {
        defaultBranchRef {
            target {
                ... on Commit {
                    history <AFTER>{
                        pageInfo{
                            endCursor
                            hasNextPage
                        }
                        nodes {
                            oid
                        }
                    }
                }
            }
        }
    }
}
"""

HISTORY_BRANCH_LIMIT_QUERY = """
query getHistory($owner: String!, $name: String!, $history_size: Int!) {
    repository(owner: $owner, name: $name) {
        defaultBranchRef {
            target {
                ... on Commit {
                    history (first: $history_size){
                        pageInfo{
                            endCursor
                            hasNextPage
                        }
                        nodes {
                            oid
                        }
                    }
                }
            }
        }
    }
}      
"""

GET_DEFAULT_BRANCH_QUERY = """
query getRepository($owner: String!, $name: String!)
        {
            repository(owner: $owner, name: $name)
            {
                name
                defaultBranchRef {
                    name
                }
            }
        }  
"""

QUERY_PARENTS_FIRST_HEADER ="""
query getCommitGraph($owner: String!, $name: String!, $oid: GitObjectID!) {
"""

QUERY_PARENTS_HEADER = """
query getCommitGraph($owner: String!, $name: String!, $oid: GitObjectID!, $after: String!) {
"""

QUERY_PARENTS = """
repository(owner: $owner, name: $name) {
        object(oid: $oid) {
            ... on Commit {
                oid
                parents(first: 100<AFTER>) {
                    pageInfo{
                        endCursor
                        hasNextPage
                    }
                    nodes {
                        oid
                    }
                }
            }
        }
    }
}              
"""
    

QUERY_PARENTS_LAST = """
    repository(owner: $owner, name: $name) {
        object(oid: $oid) {
            ... on Commit {
                oid
                parents(first: 100) {
                    pageInfo{
                        endCursor
                        hasNextPage
                    }
                    nodes {
                        oid
                    }
                }
            }
        }
    }
}              
"""