#include <stdio.h>
#include <stdlib.h>

int main() {
  char *shell = getenv("MYSHELL");
  if(shell)
    printf("SHELL(/bin/sh): 0x%x\n", (unsigned int)shell);

  shell = getenv("MYBASH");
  if(shell)
    printf("BASH(/bin/bash): 0x%x\n", (unsigned int)shell);

  shell = getenv("MYP");
  if(shell)
    printf("'-p': 0x%x\n", (unsigned int)shell);
}
