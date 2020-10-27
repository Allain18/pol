"""File containing entry point for the command line"""

import sys
import argparse
import pathlib

import rpn_calc


__version__ = "0.2.1"


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
    parser.add_argument(
        "-r", "--rounding", type=int,
        help="choose the precison of rounding, default 0", default=None)

    return parser.parse_args()


def main():
    """Entry point of the program"""
    args = get_args()

    if args.version:
        print("pol version v{}".format(__version__))
        print("Python {}".format(sys.version))
        return

    cal = rpn_calc.Calculator()

    if args.list:
        doc = "List of commands available:\n\n"
        for command, method in cal.operation.items():
            doc += "`{}` : {}\n".format(command, method.__doc__)
        print(doc)
        return

    cal.rounding_value = args.rounding

    if not args.ignore_local_config:
        file_path = pathlib.Path("{}/pol.yml".format(pathlib.Path.home()))
        if file_path.exists():
            cal.add_config(file_path)

    if isinstance(args.file, list):
        for file in args.file:
            path_file = pathlib.Path(file)
            if path_file.exists():
                cal.add_config(path_file)

    cal.loop()


if __name__ == "__main__":
    main()
