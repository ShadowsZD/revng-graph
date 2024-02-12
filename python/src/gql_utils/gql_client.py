from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from gql_utils import utils, gql_queries

class gql_client:

    def __init__(self, url: str, token: str | None = None) -> None:
        headers = None

        if token:
            headers = {'Authorization': f"Bearer {token}"}

        transport = AIOHTTPTransport(
            url=url,
            headers = headers,
        )

        self.client = Client(transport=transport, fetch_schema_from_transport=True)
    
    def get_default_branch(self, owner: str, repo_name: str) -> str:
        """
        Get default branch for owner/repo combination
        """

        params = {
            "owner": owner,
            "name": repo_name      
        }

        return self.client.execute(gql(gql_queries.GET_DEFAULT_BRANCH_QUERY), 
                                   variable_values=params)["repository"]["defaultBranchRef"]["name"]
        
    def get_branch_history(self, owner: str, name: str, history_size: int | None = None) -> list:
        """
        get branch history of commits oids and returns them in a list
        """

        params = {
            "owner": owner,
            "name": name,
            "history_size": history_size,
            "after": None
        }

        commit_oids = []
        has_next_page = True
        
        if history_size:
            if history_size > 100:
                raise Exception("Limit size 100, dont pass size if looking for all results") 
            else:
                contents = self.client.execute(gql(gql_queries.HISTORY_BRANCH_LIMIT_QUERY), variable_values=params)
                utils.add_oids(commit_oids, contents["repository"]["defaultBranchRef"]["target"]["history"]["nodes"])
                print(commit_oids)
        else:
            while(has_next_page):
                query = utils.create_query_branch_history(params["after"])
                contents = self.client.execute(query, variable_values=params)

                utils.add_oids(commit_oids, contents["repository"]["defaultBranchRef"]["target"]["history"]["nodes"])

                has_next_page = contents["repository"]["defaultBranchRef"]["target"]["history"]["pageInfo"]["hasNextPage"]
                params["after"] = contents["repository"]["defaultBranchRef"]["target"]["history"]["pageInfo"]["endCursor"]

        return commit_oids
        
    def get_commit_parent_relation(self, owner: str, name: str, commit_oids: list) -> dict:
        """
        get parents for each commit oid in given repo
        """
        params = {
            "owner": owner,
            "name": name,
        }

        commit_relation = {}

        for commit_id in commit_oids:
            params["oid"] = commit_id
            parents_oids = []

            has_next_page = True

            while(has_next_page):
                query = utils.create_query_parents(params.get("after"))
                contents = self.client.execute(query, variable_values=params)
                utils.add_oids(parents_oids, contents["repository"]["object"]["parents"]["nodes"])

                has_next_page = contents["repository"]["object"]["parents"]["pageInfo"]["hasNextPage"]

                if has_next_page:
                    params["after"] = contents["repository"]["object"]["parents"]["pageInfo"]["endCursor"]
                    
            commit_relation[commit_id] = parents_oids

        return commit_relation
        
