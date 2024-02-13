#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

extern char **environ;

void printenv() {
  int i = 0;
  while(environ[i] != NULL) {
    printf("%s\n", environ[i]);
    ++i;
  }
}

void main() {
  pid_t childPid;
  switch(childPid = fork()) {
    case 0:
      printf("Child Process\n");
      //printenv();
      exit(0);
    default:
      printf("Parent Process\n");
      printenv();
      exit(0);
  }
}
