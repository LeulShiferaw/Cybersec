#define _GNU_SOURCE

#include <stdio.h>
#include <unistd.h>

int main() {
  unsigned int flags = RENAME_EXCHANGE;

  unlink("/tmp/ABC");
  unlink("/tmp/XYZ");

  symlink("FileOne", "/tmp/ABC");
  symlink("FileTwo", "/tmp/XYZ");

  renameat2(0, "/tmp/XYZ", 0, "/tmp/ABC", flags);
  renameat2(0, "/tmp/XYZ", 0, "/tmp/ABC", flags);
  return 0;
}
