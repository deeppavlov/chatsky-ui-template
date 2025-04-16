import logging
from pathlib import Path
from platform import system
import click

from chatsky import Pipeline
from chatsky_ui.clients.context_storage import ChatskyUIContextStorage


logging.basicConfig(level=logging.INFO)


@click.command()
@click.option("--working-dir", required=True, type=Path, help="Path to the script file")
@click.option("--run-id", required=True, type=int, help="ID of this `Run` process")
def main(working_dir: Path, run_id: int):
    working_dir = Path(working_dir)
    separator = "///" if system() == "Windows" else "////"

    db_uri = f"sqlite+aiosqlite:{separator}{working_dir.absolute() / 'bot' / 'databases' / 'context_storage.db'}"
    db = ChatskyUIContextStorage(db_uri, run_id)

    pipeline = Pipeline.from_file(
        file=working_dir / "bot" / "scripts" / "build.yaml",
        custom_dir=working_dir / "bot" / "custom",
        context_storage=db,
    )
    pipeline.run()


if __name__ == "__main__":
    main()
