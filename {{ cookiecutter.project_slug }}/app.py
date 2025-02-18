import logging
from pathlib import Path
from platform import system
import click

from chatsky import Pipeline
from chatsky.context_storages import context_storage_factory
from chatsky_ui.core.config import settings


logging.basicConfig(level=logging.INFO)


@click.command()
@click.option("--script-path", required=True, help="Path to the script file")
def main(script_path: Path, run_id: int = 0):
    separator = "///" if system() == "Windows" else "////"
    db_path = Path(f"{settings.context_storage_dir}/run_{run_id}.db")
    db_uri = f"sqlite+aiosqlite:{separator}{db_path.absolute()}"
    db = context_storage_factory(db_uri)

    pipeline = Pipeline.from_file(
        file=script_path,
        custom_dir=Path(script_path).parent.parent / "custom",
        context_storage=db,
    )
    pipeline.run()


if __name__ == "__main__":
    main()
