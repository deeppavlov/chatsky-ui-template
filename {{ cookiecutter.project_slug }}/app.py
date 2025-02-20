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
@click.option("--run-id", required=True, help="Run ID")
def main(script_path: Path, run_id: int):
    separator = "///" if system() == "Windows" else "////"
    db_file = Path(f"{settings.context_storage_dir}/run_{run_id}.db")
    db_file.touch(exist_ok=True)
    db_uri = f"sqlite+aiosqlite:{separator}{db_file.absolute()}"
    db = context_storage_factory(db_uri)

    pipeline = Pipeline.from_file(
        file=script_path,
        custom_dir=Path(script_path).parent.parent / "custom",
        context_storage=db,
    )
    pipeline.run()


if __name__ == "__main__":
    main()
