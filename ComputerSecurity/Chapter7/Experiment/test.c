#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main() {
  FILE* f = fopen("A", "a+");
  unlink("A");
  symlink("B", "A");
  char str[] = "Hello World";
  fwrite(str, sizeof(char), strlen(str), f);
  return 0; 
}
