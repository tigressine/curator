"""
"""
import parser

argument_parser = parser.Parser()
argument_parser.parse_arguments()

print(argument_parser.arguments)
print(argument_parser.unknown)


"""
input_dir = Path(sys.argv[1])

def get_all_filetypes(directory):
    filetypes = set()
    add_filetypes(directory, filetypes)

    return filetypes


def add_filetypes(directory, filetypes):
    for item in directory.iterdir():
        if item.is_dir():
            add_filetypes(item, filetypes)
        else:
            filetypes.add(item.suffix)


if len(sys.argv) < 2:
    print("wrong args")
    exit(1)

if not input_dir.exists():
    print("doesnt exist")
    exit(1)

if not input_dir.is_dir():
    print("not dir")
    exit(1)

filetypes = get_all_filetypes(input_dir)
print(filetypes)
"""
