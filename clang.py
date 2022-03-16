import subprocess
import sys

def main():
    args = ["clang++"]
    args.extend(sys.argv[1:])
    subprocess.run(args)


if __name__ == "__main__":
    main()