from pathlib import Path

from chatsky import Pipeline
from chatsky.utils.testing import (
    check_happy_path,
    is_interactive_mode,
)

script_path = Path(__file__).parent / "bot/scripts/build_0.yaml"
custom_dir = Path(script_path).parent.parent / "custom"
pipeline = Pipeline.from_file(file = script_path, custom_dir = custom_dir)

HAPPY_PATH = [
    ("Hi", "Do you want pizza?"),
    ("Yes", "Great! Would you like cheese on it?")
    ("Yes", "Order placed"),
]


assert check_happy_path(
        pipeline, HAPPY_PATH, printout=True
    )

# if is_interactive_mode():
#     pipeline.run()
