import sys
from pathlib import Path
from g3p_converter.cli import main as cli_main


def main(arg1: str, arg2: str) -> None:
    input_path = Path(arg1)
    output_path = Path(arg2)

    for image in input_path.iterdir():
        if image.is_file():
            cli_main([str(image), str(output_path / (image.stem + ".g3p"))])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(f"Usage: {sys.argv[0]} <arg1> <arg2>")
    main(sys.argv[1], sys.argv[2])