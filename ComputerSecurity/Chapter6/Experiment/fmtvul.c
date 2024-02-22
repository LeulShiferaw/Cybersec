#include <stdio.h>

void fmtstr(char *str) {
  unsigned int *framep;
  unsigned int *ret;

  asm("movl %%ebp, %0" : "=r"(framep));
  ret = framep + 1;

  printf("The address of the input array: 0x%.8x\n", (unsigned)str);
  printf("The value of the frame pointer: 0x%.8x\n", (unsigned)framep);
  printf("The value of the return address: 0x%.8x\n", *ret);
  printf(str);
  printf("\nThe value of the return address: 0x%.8x\n", *ret);
}

int main(int argc, char **argv) {
  FILE *badfile;
  char str[200];

  badfile = fopen("badfile", "rb");
  fread(str, sizeof(char), 200, badfile);
  fmtstr(str);

  return 1;
}
