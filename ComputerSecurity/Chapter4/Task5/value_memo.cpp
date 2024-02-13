#include <iostream>

using namespace std;

int main() {
  cout << hex << *(int*)0x00007fffffffe0b0 << endl;
  return 0;
}
