project_dir=$(dirname $(dirname $(dirname $(dirname $(realpath $0)))))

if [ -z "$chatsky_port" ]; then
    chatsky.ui build_scenario $build_id --project-dir $project_dir --messenger $messenger
else
    chatsky.ui build_scenario $build_id --project-dir $project_dir --messenger $messenger --chatsky-port $chatsky_port
fi
