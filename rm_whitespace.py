import sys

def main():
    n = len(sys.argv)
    if n < 2:
        print("Usage: rm_whitespace.py <file_name>")
        exit(1)
    file_name = sys.argv[1]

    with open(file_name, 'r') as _file:
        lines = _file.readlines()
        for line in lines:
            print(format(line.rstrip()))
main()