from toon import encode
import os
import json, sys


def main():
    try:
        input_file = os.path.realpath(sys.argv[1])
    except Exception as invalid_usage:
        print(f"Usage: python {sys.argv[0]} file")
        sys.exit(1)

    try:
        with open(f"{input_file}", "r") as file:
            res = json.load(file)
            changed = encode(res)
            with open(f"{os.path.splitext(input_file)[0]}.toon", "w") as outfile:
                outfile.write(changed)
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
