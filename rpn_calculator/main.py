"""File containing entry point for the command line"""

import sys
import argparse
import pathlib

from .calculator import Calculator
from .version import __version__


def get_args():
    """Get the args from argparse"""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="A RPN calculator written in python\n"
        "Support decimal, hexadecimal, binary and octal"
    )

    parser.add_argument(
        "-v", "--version", help="show the version number and exit", action="store_true")
    parser.add_argument(
        "-l", "--list", help="list all commands available and exit", action="store_true")
    parser.add_argument(
        "--ignore-local-config", help="don't add commands from ~/.pol",
        action="store_true")
    parser.add_argument(
        '-f', "--file", type=str, nargs="+",
        help="file with customs commands")

    return parser.parse_args()


def main():
    """Entry point of the program"""
    args = get_args()

    if args.version:
        print("pol version v{}".format(__version__))
        print("Python {}".format(sys.version))
        return

    cal = Calculator()

    if args.list:
        doc = "List of commands available:\n\n"
        for command, method in cal.operation.items():
            doc += "`{}` : {}\n".format(command, method.__doc__)
        print(doc)
        return

    if not args.ignore_local_config:
        file_path = pathlib.Path("{}/.pol".format(pathlib.Path.home()))
        if file_path.exists():
            cal.add_commands(file_path)

    if isinstance(args.file, list):
        for file in args.file:
            path_file = pathlib.Path(file)
            if path_file.exists():
                cal.add_commands(path_file)

    cal.loop()
