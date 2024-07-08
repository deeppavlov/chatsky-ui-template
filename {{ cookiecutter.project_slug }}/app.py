import logging
from pathlib import Path
import click

from dff import Pipeline


logging.basicConfig(level=logging.INFO)


@click.command()
@click.option("--script-path", required=True, help="Path to the script file")
def main(script_path: str):
    script_file = Path(__file__).parent / script_path
    pipeline = Pipeline.from_file(script_file)
    pipeline.run()


if __name__ == "__main__":
    main()
