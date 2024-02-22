#include <stdio.h>

void fmtstr() {
  char input[100];
  int var = 0x11223344;

#if __x86_64__
  printf("Target address: 0x%.161x\n", (unsigned long) &var);
#else
  printf("Target address: 0x%.8x\n", (unsigned int)&var);
#endif

  printf("Data at target address: 0x%x\n", var);
  printf("Please enter a string: ");
  fgets(input, sizeof(input), stdin);
  printf(input);
  printf("Data at target address: 0x%x\n", var);
}

void main() {
  fmtstr();
}
