project_dir=$(dirname $(dirname $(dirname $(dirname $(realpath $0)))))

chatsky.ui run_scenario --project-dir $project_dir --run-id $run_id
