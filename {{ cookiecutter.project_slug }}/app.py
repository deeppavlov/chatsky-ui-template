import logging
from pathlib import Path
from platform import system
import click

from chatsky import Pipeline
from chatsky.context_storages import context_storage_factory
from context_storage import ChatskyUIContextStorage


logging.basicConfig(level=logging.INFO)


@click.command()
@click.option("--script-path", required=True, type=Path, help="Path to the script file")
@click.option("--dialogue-db-path", required=True, type=Path, help="Path to the context storage")
@click.option("--run-id", required=True, type=int, help="ID of this `Run` process")
def main(script_path: Path, dialogue_db_path: Path, run_id: int):
    separator = "///" if system() == "Windows" else "////"

    # TODO: (decide before merge) 'dialogue_db_path.absolute' could just be settings.database_path,
    # which removes an unnecessary parameter, making the code easier to read.
    # But I'm not sure if that's correct, so I placed this comment here.
    db_uri = f"sqlite+aiosqlite:{separator}{dialogue_db_path.absolute()}"
    # db = context_storage_factory(db_uri)
    db = ChatskyUIContextStorage(db_uri, run_id)

    pipeline = Pipeline.from_file(
        file=script_path,
        custom_dir=Path(script_path).parent.parent / "custom",
        context_storage=db,
    )
    pipeline.run()


if __name__ == "__main__":
    main()
