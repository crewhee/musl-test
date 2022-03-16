#include <iostream>

#ifndef AA
#define AA
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

int main(){
}
