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
    else: # not sure if this one works, so use default bootstrap
        if os.isfile(path + "bin/clang"):
            args.append(f"CMAKE_C_COMPILER={path + "bin"}/clang")
        if os.isfile(path + "bin/clang"):
            args.append(f"CMAKE_CXX_COMPILER={path + "bin"}/clang++")
    print(args)
    subprocess.run(args)
    args2 = ["make", "stage2"]
    args2.append("-j" + str(multiprocessing.cpu_count()))
    subprocess.run(args2)



if __name__ == "__main__":
    main()