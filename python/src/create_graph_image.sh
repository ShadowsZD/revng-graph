#!/bin/bash

DOT_EXECUTABLE=$(where dot)

# Check if dot was found
if [ -z "$DOT_EXECUTABLE" ]; then
    echo "Error: dot executable not found in the PATH."
    exit 1
fi

$DOT_EXECUTABLE -Tpng commit_graph.dot -o graph.png