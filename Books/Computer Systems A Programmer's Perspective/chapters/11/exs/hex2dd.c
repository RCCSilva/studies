// Chapater 11 - Ex 11.2

#include <stdlib.h>
#include <stdio.h>

void main(int argc, char **argv) 
{
    unsigned short dd = (int) strtol(argv[1], NULL, 16);
    printf("%i\n", dd);
}