from gql_utils.gql_client import gql_client
import graph_utils.graph_utils as graph_utils
import argparse

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('repo_owner', type=str, help='Owner of the repo')
    parser.add_argument('repo', type=str, help='Repo name')

    parser.add_argument('--token',  help='Personal GitHub token for authentication')

    args = parser.parse_args()

    client = gql_client("https://api.github.com/graphql", args.token)
    print(f"Default branch for repo {args.repo}, owner {args.repo_owner}: {client.get_default_branch(args.repo_owner, args.repo)}")
    
    commit_oids = client.get_branch_history( args.repo_owner, args.repo)

    relations = client.get_commit_parent_relation(args.repo_owner, args.repo, commit_oids)

    graph_utils.create_graph_file(relations)
    if graph_utils.is_acyclic_graph(relations):
        print("Graph is acyclic")
    else:
        print("Not acyclic")

if __name__ == "__main__":
    main()