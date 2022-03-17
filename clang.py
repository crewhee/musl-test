import subprocess
import sys
from os.path import isfile
from os import remove

code = """
#ifndef PRINT_COMPILE_DATETIME
#define PRINT_COMPILE_DATETIME
#ifndef _GLIBCXX_IOSTREAM
#include <iostream>
#endif

class ThisIsVeryBadStyleIHopeNobodyWantsThisName {
public:
      ThisIsVeryBadStyleIHopeNobodyWantsThisName() {
           std::cout << "Build with Clang, " << __DATE__ << " " << __TIME__ << std::endl;
      }    
};    
ThisIsVeryBadStyleIHopeNobodyWantsThisName thisIsVeryBadStyleIHopeNobodyWantsThisName;
#endif
"""

def main():
    NAME = "DATETIME"
    while(isfile(NAME + ".cpp")):
        NAME += "1"
    with open(NAME + ".cpp", 'w') as f:
        f.write(code)
    args = ["clang++"]
    args.extend(sys.argv[1:])
    args.extend(["--include", NAME + ".cpp"])
    subprocess.run(args)
    remove(NAME + ".cpp")


if __name__ == "__main__":
    main()