#include <iostream>

using namespace std;

int main() {
  int n = 1;
  if (*(char*)&n == 1) {
    cout << "Little Endian" << endl;
  } else cout << "Big Endian" << endl;
}
