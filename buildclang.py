import subprocess
import multiprocessing
import sys
import os


def main():
    # add build directory
    path = os.getcwd() + "/build"
    if not os.path.isdir(path):
        os.mkdir(path, 777)
    os.chdir(path)

    args = ["cmake"]
    if len(sys.argv) > 1:
        args.append(sys.argv[1])
    else:
        args.append("../")
    args.extend(["-G", "Unix Makefiles"])
    bootstrap = True
    if bootstrap:
        args.append("-DCLANG_ENABLE_BOOTSTRAP=On")
    else: # not sure if this one works, so use default bootstrap move
        current_dir_ls = subprocess.run(["ls", path[0:-6]], capture_output=True).stdout.split(b'\n')
        if b'clang' in current_dir_ls:
            args.append("CMAKE_C_COMPILER=./clang")
        if b'clang++' in current_dir_ls:
            args.append("CMAKE_CXX_COMPILER=./clang++")
    print(args)
    subprocess.run(args)
    args2 = ["make", "stage2"]
    args2.append("-j" + str(multiprocessing.cpu_count()))
    subprocess.run(args2)



if __name__ == "__main__":
    main()