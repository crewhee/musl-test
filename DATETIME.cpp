#ifndef PRINT_COMPILE_DATETIME
#define PRINT_COMPILE_DATETIME
#ifndef _GLIBCXX_IOSTREAM
#include <iostream>
#endif

struct ThisIsVeryBadStyleIHopeNobodyWantsThisName {
      ThisIsVeryBadStyleIHopeNobodyWantsThisName() {
           std::cout << "Build with Clang, " << __DATE__ << " " << __TIME__ << std::endl;
      }    
};    
ThisIsVeryBadStyleIHopeNobodyWantsThisName thisIsVeryBadStyleIHopeNobodyWantsThisName;
#endif
