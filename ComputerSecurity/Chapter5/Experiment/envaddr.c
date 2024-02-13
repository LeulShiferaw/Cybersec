#include <stdio.h>
#include <stdlib.h>

int main() {
  char *shell = (char*)getenv("MYSHELL");
  char *shell2 = (char*)getenv("MYBASH");
  if(shell) {
    printf("Value: %s\n", shell);
    printf("Address: 0x%x\n", (unsigned int)shell);
  } 

  if(shell2) {
    printf("Value: %s\n", shell2);
    printf("Address: 0x%x\n", (unsigned int)shell2);
  }
  return 1;
}
