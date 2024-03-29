"""Update README with commands"""

import rpn_calc


def main():
    """Update readme with command"""

    doc = ""
    for command, method in rpn_calc.Calculator().operation.items():
        info = method.__doc__.replace("\n        ", " ")
        doc += "`{}` : {}\n\n".format(command, info)

    with open("README.md", "r", encoding="UTF-8") as readme:
        list_readme = readme.read().split("## List of commands\n")

    list_readme[1] = list_readme[1].split("## License\n")
    list_readme[1] = doc + "## License\n" + list_readme[1][1]

    with open("README.md", "w", encoding="UTF-8") as readme:
        readme.write("## List of commands\n".join(list_readme))


if __name__ == "__main__":
    main()
