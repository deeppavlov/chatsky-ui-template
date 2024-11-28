project_dir=$(dirname $(dirname $(dirname $(dirname $(realpath $0)))))

chatsky.ui build_scenario --project-dir $project_dir
