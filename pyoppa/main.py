import sys
from oppa import Oppa 

def main():
    if len(sys.argv) != 2:
        print("Usage: Oppa <filename.oppa>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, "r", encoding="UTF-8") as file:
        code = file.read()

    interpreter = Oppa()
    interpreter.compile(code)

if __name__ == "__main__":
    main()