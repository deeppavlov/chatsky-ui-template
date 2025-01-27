project_dir=$(dirname $(dirname $(dirname $(dirname $(realpath $0)))))

if [ -z "$chatsky_port" ]; then
    chatsky.ui build_scenario --project-dir $project_dir
else
    chatsky.ui build_scenario --project-dir $project_dir --chatsky-port $chatsky_port
fi
