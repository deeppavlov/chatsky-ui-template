#!/bin/bash
if [ $# -eq 0 ]; then
    echo "Usage: $0 BUILD_ID"
    exit 1
fi

# Assign the first argument to the variable
build_id=$1

dflowd run_scenario $build_id --project-dir .
# poetry run df_d run