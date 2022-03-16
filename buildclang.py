import subprocess


def main():
    args = ["cmake", "."]
    current_dir_ls = subprocess.run("ls", capture_output=True).stdout.split(b'\n')
    if b'clang' in current_dir_ls:
        args.append("CMAKE_C_COMPILER=clang")
    if b'clang++' in current_dir_ls:
        args.append("CMAKE_CXX_COMPILER=clang++")
    subprocess.run(args)
    subprocess.run("make")



if __name__ == "__main__":
    main()