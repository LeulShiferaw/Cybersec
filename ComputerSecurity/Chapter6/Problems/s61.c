#include <stdio.h>
#include <string.h>
#include <stdarg.h>

void var_func(int Narg, ...) {
  va_list ap;
  va_start(ap, Narg);

  int res = 0;

  int i;
  for(i = 0; i<Narg; ++i) {
    res += strlen(va_arg(ap, char *));
  }

  va_end(ap);
  
  printf("%d\n", res);
}

int main() {
  var_func(4, "hello", "when", "where", "why");
  return 0;
}
