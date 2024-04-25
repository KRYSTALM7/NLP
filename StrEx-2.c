#include <stdio.h>
#include <string.h>

int main() {
  char source[100] = "Hello World";
  char destination[100];

  strcpy(destination, source);

  printf("Source string: %s\n", source);
  printf("Destination string: %s\n", destination);
  
  return 0;
}

