## Info
Program to generate commit history from a given Git repository

Usage:
```
python main.py --token [YOUR_TOKEN] [GIT_REPO_OWNER] [GIT_REPO_NAME]
```

## Outputs
Generates graph dot file and prints to console if graph is acyclic or not

## Generate graph image
Windows:
```
create_graph_image.bat
```

Linux:
```
./create_graph_image.sh
```

The output will be a png file called graph.png with the relations
