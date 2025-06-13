import numpy as np
import typer


def main(name: str):
    print(f"hello {name}, my numpy version is: {np.__version__}")


if __name__ == "__main__":
    typer.run(main)
