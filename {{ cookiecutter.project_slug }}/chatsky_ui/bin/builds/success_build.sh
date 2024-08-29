#!/bin/bash
if [ $# -eq 0 ]; then
    echo "Usage: $0 BUILD_ID"
    exit 1
fi

# Assign the first argument to the variable
build_id=$1
project_dir=$(dirname $(dirname $(dirname $(dirname $(realpath $0)))))

chatsky.ui build_scenario $build_id --project-dir $project_dir
