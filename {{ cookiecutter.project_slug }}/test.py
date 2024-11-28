from pathlib import Path

from chatsky import Pipeline
from chatsky.utils.testing import check_happy_path

script_path = Path(__file__).parent / "bot/scripts/build.yaml"
custom_dir = Path(script_path).parent.parent / "custom"
pipeline = Pipeline.from_file(file = script_path, custom_dir = custom_dir)

HAPPY_PATH = [
    ("/start", "Hello!"),
    ("hello", "Do you want a pizza?"),
    ("yes", "Some cheese in pizza?"),
    ("yes", "Cool! Your order is coming!"),
]


check_happy_path(
        pipeline, HAPPY_PATH, printout=True
    )
