"""Update README with commands"""

import calculator


def main():
    """Update readme with command"""

    doc = ""
    for command, method in calculator.Calculator().operation.items():
        doc += "__\"{}\"__: {}\n\n".format(command, method.__doc__)

    with open("README.md", "r") as readme:
        list_readme = readme.read().split("## List of commands\n")

    list_readme[1] = list_readme[1].split("## License\n")
    list_readme[1] = doc + "## License\n" + list_readme[1][1]

    with open("README.md", "w") as readme:
        readme.write("## List of commands\n".join(list_readme))


if __name__ == "__main__":
    main()
