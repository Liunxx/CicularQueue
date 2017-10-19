import sys
from CircularQueue import CircularQueue


def main():
    fp = open(input("Insert Filename (with extension) for input: ").strip())
    output = sys.stdout

    # comment back in for writing output to the file, mandatory for grading purposes.
    # output = open(input("Insert Filename (with extension) for output: ").strip(), 'w')

    q = CircularQueue()
    for command in fp.readlines():
        q.parse_command(command.strip('\n'))
        print(q, file=output)
    fp.close()


main()
