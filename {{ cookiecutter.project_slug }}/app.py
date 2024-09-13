import logging
from pathlib import Path
import click

from chatsky import Pipeline


logging.basicConfig(level=logging.INFO)


@click.command()
@click.option("--script-path", required=True, help="Path to the script file")
def main(script_path: Path):
    pipeline = Pipeline.from_file(file = script_path, custom_dir = Path(script_path).parent.parent / "custom")
    pipeline.run()


if __name__ == "__main__":
    main()
