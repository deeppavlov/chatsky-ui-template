import logging
from pathlib import Path
from platform import system
import click

from chatsky import Pipeline
from chatsky.context_storages import context_storage_factory


logging.basicConfig(level=logging.INFO)


@click.command()
@click.option("--script-path", required=True, type=Path, help="Path to the script file")
@click.option("--dialogue-db-path", required=True, type=Path, help="Path to the context storage")
def main(script_path: Path, dialogue_db_path: Path):
    separator = "///" if system() == "Windows" else "////"

    db_uri = f"sqlite+aiosqlite:{separator}{dialogue_db_path.absolute()}"
    db = context_storage_factory(db_uri)

    pipeline = Pipeline.from_file(
        file=script_path,
        custom_dir=Path(script_path).parent.parent / "custom",
        context_storage=db,
    )
    pipeline.run()


if __name__ == "__main__":
    main()
