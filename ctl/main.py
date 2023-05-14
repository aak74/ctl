from typing import Annotated
import typer

from ctl.dispatcher import dispatch

app = typer.Typer()


@app.command()
def apply(filename: Annotated[str, typer.Option("--filename", "-f")]):
    dispatch(filename)


@app.command()
def about():
    print(f"Try ctl")


def main():
    app()


if __name__ == "__main__":
    app()
